#!/bin/bash
#SBATCH --account=nnt250008
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --job-name=P2_static_R3
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err

set -euo pipefail

module --force purge
module load gcc/11.2.0 openmpi/4.1.6
module load intel-mkl/2020.4.304

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE

VASP_BIN="$HOME/vasp/6.3.2/vasp.6.3.2/bin/vasp_std"

if [ ! -x "$VASP_BIN" ]; then
    echo "ERROR: VASP executable missing"
    exit 1
fi

if ldd "$VASP_BIN" | grep -q "not found"; then
    echo "ERROR: Unresolved VASP libraries"
    exit 1
fi

cd "$SLURM_SUBMIT_DIR"

echo "Starting P2 parent PBE+U pre-relaxation"
echo "VASP binary: $VASP_BIN"
echo "MPI ranks: $SLURM_NTASKS"
module list

srun -n "$SLURM_NTASKS" --kill-on-bad-exit "$VASP_BIN"
