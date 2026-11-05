#!/usr/bin/env python
"""
Ewald-ranked ordered candidates for P2-Na0.67Fe0.5Mn0.5O2 in a 3x3x1 cell (Na12 Fe9 Mn9 O36).

The P2 cell (P6_3/mmc) is built from its Wyckoff positions:
  TM 2a (0,0,0) | O 4f (1/3,2/3,z) | Na_f 2b (0,0,1/4) | Na_e 2d (1/3,2/3,3/4)
A Na_f site and its three Na_e neighbours are 1.69 A apart, so they are never occupied together.

Stage 1  simulated annealing of Na (fixed Na_f:Na_e split) and Fe/Mn together on a
         precomputed Ewald matrix, with Fe at +3 and Mn at its average, +11/3
Stage 2  place 3 Mn3+ and 6 Mn4+ among the 9 Mn (all 84 choices checked)
Ewald energies are a pre-filter only; DFT decides which candidate is lowest.

Usage (note in your log where a, c and z_O come from):
  python generate_p2_parent.py --a 2.933 --c 11.223 --zO 0.092 --splits 4:8 6:6 2:10 --out ordered_candidates
"""
import argparse
import csv
import itertools
import warnings
from pathlib import Path

import numpy as np
from pymatgen.analysis.ewald import EwaldSummation
from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.core import Lattice, Structure
from pymatgen.io.vasp import Poscar

warnings.filterwarnings("ignore")

N_NA, N_FE = 12, 9
Q_NA, Q_FE, Q_MN, Q_O = 1.0, 3.0, 11 / 3, -2.0
MAGMOM = "12*0 9*5 3*4 6*3 36*0"   # Na, Fe3+, Mn3+ (listed first), Mn4+, O


def host(a, c, z_o):
    """Every candidate site of the 3x3x1 cell; Li marks Na_e sites until output."""
    s = Structure.from_spacegroup(
        "P6_3/mmc", Lattice.hexagonal(a, c), ["Mn", "O", "Na", "Li"],
        [[0, 0, 0], [1 / 3, 2 / 3, z_o], [0, 0, 0.25], [1 / 3, 2 / 3, 0.75]])
    s.make_supercell([3, 3, 1])
    return s


class Sampler:
    def __init__(self, s, n_f, n_e, rng):
        sym = [site.specie.symbol for site in s]
        self.tm = np.array([i for i, x in enumerate(sym) if x == "Mn"])
        self.o = np.array([i for i, x in enumerate(sym) if x == "O"])
        self.naf = np.array([i for i, x in enumerate(sym) if x == "Na"])
        self.nae = np.array([i for i, x in enumerate(sym) if x == "Li"])
        self.n_f, self.n_e, self.rng = n_f, n_e, rng
        unit = s.copy()
        unit.add_oxidation_state_by_site([1.0] * len(unit))
        self.M = EwaldSummation(unit).total_energy_matrix      # E = q @ M @ q
        d = s.distance_matrix
        self.block = {int(i): {int(j) for j in self.nae if d[i, j] < 2.0} for i in self.naf}
        self.block.update({int(j): {int(i) for i in self.naf if d[i, j] < 2.0} for j in self.nae})

    def random_state(self):
        for _ in range(1000):
            q = np.zeros(len(self.M))
            q[self.o] = Q_O
            q[self.tm] = Q_MN
            q[self.rng.choice(self.tm, N_FE, replace=False)] = Q_FE
            occ = set()
            order = [(self.nae, self.n_e), (self.naf, self.n_f)]
            if self.rng.random() < 0.5:
                order.reverse()
            for pool, n in order:
                free = [int(i) for i in self.rng.permutation(pool) if not self.block[int(i)] & occ]
                if len(free) < n:
                    break
                occ |= set(free[:n])
            else:
                q[list(occ)] = Q_NA
                return q
        raise RuntimeError("could not place Na without Na_f/Na_e clashes")

    def anneal(self, steps, t_hi=1.0, t_lo=0.005):
        M, rng = self.M, self.rng
        q = self.random_state()
        mq = M @ q
        e = float(q @ mq)
        best_q, best_e = q.copy(), e
        p_f = self.n_f / (self.n_f + self.n_e)
        for t in np.geomspace(t_hi, t_lo, steps):
            if rng.random() < 0.5:                      # swap an Fe and an Mn
                a = rng.choice(self.tm[q[self.tm] == Q_FE])
                b = rng.choice(self.tm[q[self.tm] == Q_MN])
                da, db = Q_MN - Q_FE, Q_FE - Q_MN
            else:                                       # move one Na within its sublattice
                pool = self.naf if rng.random() < p_f else self.nae
                full, empty = pool[q[pool] > 0], pool[q[pool] == 0]
                if not len(full) or not len(empty):
                    continue
                a, b = rng.choice(full), rng.choice(empty)
                if any(q[j] > 0 for j in self.block[int(b)]):
                    continue
                da, db = -Q_NA, Q_NA
            de = (2 * (da * mq[a] + db * mq[b])
                  + da * da * M[a, a] + db * db * M[b, b] + 2 * da * db * M[a, b])
            if de <= 0 or rng.random() < np.exp(-de / t):
                q[a] += da
                q[b] += db
                mq += da * M[:, a] + db * M[:, b]
                e += de
                if e < best_e:
                    best_q, best_e = q.copy(), e
        return best_q, best_e

    def place_mn3(self, q):
        """Try every way of making 3 of the 9 Mn into Mn3+; return the lowest."""
        mn = [int(i) for i in self.tm if q[i] == Q_MN]
        best = None
        for mn3 in itertools.combinations(mn, 3):
            qq = q.copy()
            qq[mn] = 4.0
            qq[list(mn3)] = 3.0
            e = float(qq @ self.M @ qq)
            if best is None or e < best[1]:
                best = (set(mn3), e)
        return best


def build(s, q, fe_sites, mn3_sites):
    """Ordered structure, sites sorted Na, Fe, Mn3+, Mn4+, O, with oxidation states."""
    rows = []
    for i, site in enumerate(s):
        sym = site.specie.symbol
        if sym in ("Na", "Li"):
            if q[i] > 0:
                rows.append((0, "Na", 1, site.frac_coords))
        elif sym == "Mn":
            if i in fe_sites:
                rows.append((1, "Fe", 3, site.frac_coords))
            elif i in mn3_sites:
                rows.append((2, "Mn", 3, site.frac_coords))
            else:
                rows.append((3, "Mn", 4, site.frac_coords))
        else:
            rows.append((4, "O", -2, site.frac_coords))
    rows.sort(key=lambda r: r[0])
    out = Structure(s.lattice, [r[1] for r in rows], [r[3] for r in rows])
    out.add_oxidation_state_by_site([r[2] for r in rows])
    return out


def min_na_na(structure):
    na = [i for i, site in enumerate(structure) if site.specie.symbol == "Na"]
    return min(structure.get_distance(i, j) for k, i in enumerate(na) for j in na[k + 1:])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--a", type=float, required=True, help="hexagonal a (A) from a cited refinement")
    ap.add_argument("--c", type=float, required=True, help="hexagonal c (A) from a cited refinement")
    ap.add_argument("--zO", type=float, required=True, help="O 4f z coordinate from a cited refinement")
    ap.add_argument("--splits", nargs="+", default=["4:8"], help="Na_f:Na_e counts that sum to 12")
    ap.add_argument("--keep", type=int, default=3, help="distinct candidates kept per split")
    ap.add_argument("--restarts", type=int, default=30, help="independent annealing runs per split")
    ap.add_argument("--steps", type=int, default=20000, help="Monte Carlo steps per run")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out", default="ordered_candidates")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    s = host(args.a, args.c, args.zO)
    rng = np.random.default_rng(args.seed)
    matcher = StructureMatcher(primitive_cell=False)
    rows, worst_check = [], 0.0

    for split in args.splits:
        n_f, n_e = (int(x) for x in split.split(":"))
        if n_f + n_e != N_NA:
            raise SystemExit(f"split {split} must sum to {N_NA}")
        sampler = Sampler(s, n_f, n_e, rng)
        finals = []
        for _ in range(args.restarts):
            q, _ = sampler.anneal(args.steps)
            fe = {int(i) for i in sampler.tm if q[i] == Q_FE}
            mn3, e = sampler.place_mn3(q)
            finals.append((e, q, fe, mn3))
        finals.sort(key=lambda f: f[0])
        kept = []
        for e, q, fe, mn3 in finals:      # lowest final energy first; skip repeats
            st = build(s, q, fe, mn3)
            is_duplicate = any(
                matcher.fit(st, previous)
                for previous, _ in kept
            )
            if not is_duplicate:
                kept.append((st, e))
            if len(kept) == args.keep:
                break

        if not kept:
            raise RuntimeError(f"No candidates retained for Na split {split}")

        for rank, (st, e) in enumerate(kept):
            check = EwaldSummation(st).total_energy
            worst_check = max(worst_check, abs(check - e))
            tag = f"f{n_f}e{n_e}_{rank}"
            plain = st.copy()
            plain.remove_oxidation_states()
            Poscar(plain, comment=f"P2 Na12Fe9Mn9O36 {tag} Ewald {e:.4f} eV").write_file(out / f"POSCAR_{tag}")
            rows.append({"id": tag, "Na_f": n_f, "Na_e": n_e, "E_ewald_eV": round(e, 4),
                         "min_Na_Na_A": round(min_na_na(st), 3),
                         "formula": plain.composition.formula.replace(" ", ""), "MAGMOM": MAGMOM})
        print(f"[split {split}] kept {len(kept)} distinct; lowest Ewald {kept[0][1]:.3f} eV")

    rows.sort(key=lambda r: r["E_ewald_eV"])
    e0 = rows[0]["E_ewald_eV"]
    for r in rows:
        r["dE_meV_per_atom"] = round(1000 * (r["E_ewald_eV"] - e0) / 66, 1)
    with open(out / "summary.csv", "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} candidates in {out}/ (ranked in summary.csv); "
          f"matrix vs direct Ewald check: max |diff| = {worst_check:.2e} eV")


if __name__ == "__main__":
    main()
