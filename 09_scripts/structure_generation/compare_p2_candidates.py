from pathlib import Path
from itertools import combinations
import csv

from pymatgen.core import Structure

folder = Path("02_structures/parent_1to1/ordered_candidates")
paths = sorted(folder.glob("POSCAR_*"))

def key(site):
    return tuple(round(float(x % 1), 5) for x in site.frac_coords)

patterns = {}

for path in paths:
    s = Structure.from_file(path)

    na = [x for x in s if x.specie.symbol == "Na"]
    fe = [x for x in s if x.specie.symbol == "Fe"]
    mn = [x for x in s if x.specie.symbol == "Mn"]

    assert len(na) == 12
    assert len(fe) == 9
    assert len(mn) == 9

    # Generator places Mn3+ first, followed by Mn4+
    patterns[path.stem] = {
        "Na": {key(x) for x in na},
        "Fe": {key(x) for x in fe},
        "Mn3": {key(x) for x in mn[:3]},
    }

rows = []

print("\nPAIRWISE CONFIGURATION DIFFERENCES")
print("-" * 75)

names = list(patterns)

for a, b in combinations(names, 2):
    pa, pb = patterns[a], patterns[b]

    changes = {
        site: len(pa[site] ^ pb[site]) // 2
        for site in ("Na", "Fe", "Mn3")
    }

    print(
        f"{a:15s} vs {b:15s} | "
        f"Na changes={changes['Na']:2d} | "
        f"Fe changes={changes['Fe']:2d} | "
        f"Mn3 changes={changes['Mn3']:2d}"
    )

    rows.append({
        "candidate_A": a,
        "candidate_B": b,
        "Na_site_changes": changes["Na"],
        "Fe_site_changes": changes["Fe"],
        "Mn3_site_changes": changes["Mn3"],
    })

out = folder / "pairwise_configuration_differences.csv"

with open(out, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("\nSaved:", out)
