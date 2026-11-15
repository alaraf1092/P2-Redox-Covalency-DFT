# Reproducibility and Data Management

## Computing platform

Calculations were performed using VASP 6.3.2
on Purdue Anvil.

Research project root:

/anvil/projects/x-nnt250008/P2_Redox_Covalency

Parent benchmark calculation directory:

04_jobs/benchmark/parent_p2_x067/

## Job verification

Check Slurm status:

sacct -j JOB_ID \
  --format=JobID,JobName,State,ExitCode,Elapsed

Check final energy:

grep 'free  energy   TOTEN' OUTCAR | tail -1

Check ionic convergence:

grep 'reached required accuracy' OUTCAR

Check total magnetic moment:

grep 'number of electron' OUTCAR | tail -1

Check the final force block separately before
claiming a specific force threshold was met.

## Environment

A dedicated structural analysis environment exists:

/anvil/projects/x-nnt250008/software_envs/p2-structure

It includes pymatgen and spglib for structural
matching and analysis.

## Verified research archive

Archive checkpoint:

parent_p2_benchmark_checkpoint_20261112T164628Z.tar.gz

Location:

05_results/parent_benchmark/archives/

The archive was verified by SHA256 checksum.

It contains selected reproducibility inputs,
text outputs, Slurm logs and controlled seeding data.

The original full VASP calculations remain on Anvil.

## Data restrictions

Do not distribute or commit licensed POTCAR files.

Avoid committing:
- POTCAR
- CHGCAR
- WAVECAR
- Large raw VASP outputs
- Private credentials
- Research archives containing bulk outputs

The portable benchmark archive is retained on
Anvil rather than committed to GitHub.

## Scientific interpretation

The parent benchmark is a verified checkpoint,
not proof of a global ground-state configuration.

Final dense statics on the tight-relaxed geometries
completed as Run05E and Run06F. Further magnetic
sampling and electronic analyses remain pending.
