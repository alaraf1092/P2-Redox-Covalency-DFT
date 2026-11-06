#!/bin/bash
#SBATCH --account=nnt250008
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=4G
#SBATCH --time=02:00:00
#SBATCH --job-name=P2_Bader
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err

set -euo pipefail

module load gcc/11.2.0
export PATH="$HOME/.local/bin:$PATH"

RUN3=/anvil/projects/x-nnt250008/P2_Redox_Covalency/04_jobs/benchmark/parent_p2_x067/run03_static_pbeu_d3zero_3x3x2
BDIR=$RUN3/bader_analysis

cd "$BDIR"

echo "===== REFERENCE DENSITY ====="
if [ ! -s CHGCAR_sum ]; then
    chgsum.pl "$RUN3/AECCAR0" "$RUN3/AECCAR2"
fi

test -s CHGCAR_sum

echo
echo "===== RUNNING BADER DIRECTLY ====="
"$HOME/.local/bin/bader" "$RUN3/CHGCAR" -ref CHGCAR_sum

test -s ACF.dat

echo
echo "===== EXTRACTING ATOMIC CHARGES ====="

python3 - <<'PY'
import csv

rows = []
with open("ACF.dat") as f:
    for line in f:
        p = line.split()
        if p and p[0].isdigit() and len(p) >= 7:
            rows.append((int(p[0]), float(p[4])))

if len(rows) != 66:
    raise SystemExit(f"Expected 66 atoms, got {len(rows)}")

species = (
    ["Na"]*12 + ["Fe"]*9 + ["Mn"]*9 + ["O"]*36
)

with open("bader_charges.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["atom", "species", "bader_electrons"])
    for (atom, charge), element in zip(rows, species):
        w.writerow([atom, element, f"{charge:.6f}"])

print("Atoms:", len(rows))
print("Integrated Bader population:", f"{sum(q for _,q in rows):.6f}")

for el in ["Na", "Fe", "Mn", "O"]:
    vals = [q for (i,q), e in zip(rows,species) if e == el]
    print(f"{el}: mean Bader population = {sum(vals)/len(vals):.6f}")
PY

echo
echo "===== BADER COMPLETE ====="
ls -lh ACF.dat bader_charges.csv CHGCAR_sum
