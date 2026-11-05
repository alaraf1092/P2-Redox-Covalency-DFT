#!/usr/bin/env python3

import csv
from pathlib import Path
from itertools import combinations
from collections import Counter

from pymatgen.core import Structure
from pymatgen.analysis.ewald import EwaldSummation
from pymatgen.analysis.structure_matcher import StructureMatcher

folder = Path("02_structures/parent_1to1/ordered_candidates")
files = sorted(folder.glob("POSCAR_*"))

expected = {"Na": 12, "Fe": 9, "Mn": 9, "O": 36}

# POSCAR order: Na, Fe, Mn3+, Mn4+, O
charges = (
    [1] * 12
    + [3] * 9
    + [3] * 3
    + [4] * 6
    + [-2] * 36
)

assert len(files) == 9, f"Expected 9 candidates, found {len(files)}"

results = {}

for path in files:
    structure = Structure.from_file(path)
    counts = Counter(site.specie.symbol for site in structure)

    if len(structure) != 66 or dict(counts) != expected:
        raise ValueError(f"Incorrect composition: {path.name}")

    structure.add_oxidation_state_by_site(charges)

    energy = EwaldSummation(structure).total_energy

    results[path.name] = {
        "structure": structure,
        "energy": energy,
        "split": path.stem.split("_")[0][1:]
    }

minimum = min(x["energy"] for x in results.values())

print("\n========== HIGH-PRECISION EWALD RANKING ==========")
print(f"{'Candidate':<18}{'Ewald (eV)':>18}{'dE (meV/atom)':>20}")

for name, item in sorted(
    results.items(), key=lambda x: x[1]["energy"]
):
    delta = 1000 * (item["energy"] - minimum) / 66
    print(f"{name:<18}{item['energy']:>18.10f}{delta:>20.6f}")

# Check symmetry-equivalent structures.
matcher = StructureMatcher(
    primitive_cell=False,
    scale=False,
    attempt_supercell=False
)

print("\n========== SYMMETRY MATCHING ==========")

matches = []

for (name1, item1), (name2, item2) in combinations(
    results.items(), 2
):
    if matcher.fit(item1["structure"], item2["structure"]):
        matches.append((name1, name2))
        print(f"Equivalent under StructureMatcher: {name1} / {name2}")

if not matches:
    print("No symmetry-equivalent pairs detected.")

# Save full-precision results.
output = folder / "high_precision_audit.csv"

with open(output, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "candidate",
        "ewald_energy_eV",
        "delta_meV_per_atom"
    ])

    for name, item in sorted(
        results.items(), key=lambda x: x[1]["energy"]
    ):
        delta = 1000 * (item["energy"] - minimum) / 66
        writer.writerow([name, f"{item['energy']:.12f}", f"{delta:.8f}"])

print(f"\nSaved: {output}")
