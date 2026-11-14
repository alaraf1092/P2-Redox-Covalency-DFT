# Project Status

Project: P2 Redox Inventory vs Covalency

## Platform

Purdue Anvil HPC

## Completed

- Project directory and Git repository initialized
- Parent 66-atom P2 structure constructed
- VASP PBE+U benchmark calculations completed
- Variable-cell PBE+U+D3 parent relaxation completed
- Matched static calculations completed
- Bader and Mn-O distortion analyses performed
- Controlled Jahn-Teller seeding tests completed
- Run05D and Run06E tight relaxations completed
- Symmetry-aware structural comparisons performed
- Verified parent benchmark archive created

## Selected results

Lowest tested matched static solution:
Run03 = -422.66929102 eV/cell

Matched tight relaxation energies:

Run05D = -422.39325923 eV/cell
Run06E = -422.33357056 eV/cell

Energy separation:
59.68867 meV/cell = 3.3160 meV/f.u.

Both tight-relaxed branches retain higher
Mn moments at sites 22, 24 and 29.

## Pending

- Final dense statics on tight geometries
- Additional magnetic configuration sampling
- Orbital and projected DOS analysis
- D3 literature-method verification
- Desodiation and oxygen redox calculations
- Mg, Al, Si and Ti doping comparisons
- P2/O2 stability analysis

## Scientific caution

Run03 is the lowest among configurations tested
under the matched static protocol, not a proven
global ground state.

Distinct metastable minima have not been proven.

## Archive

Verified on 2026-11-12.

File:
parent_p2_benchmark_checkpoint_20261112T164628Z.tar.gz

Location:
05_results/parent_benchmark/archives/
