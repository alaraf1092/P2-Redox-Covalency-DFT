# P2 Fe-Mn Cathode: Parent Structure Benchmark

## Research system

P2-type Na0.667Fe0.5Mn0.5O2 sodium-ion cathode.

Simulation cell:
- Na12Fe9Mn9O36
- 66 atoms
- 18 formula units

## Research motivation

This project investigates whether redox inventory or
metal-oxygen covalency better explains structural and
oxygen stability during deep desodiation.

The initial methodology is informed by the Oxford
research of Chakraborty, House and Islam (2025).

Reference DOI:
https://doi.org/10.1039/D5TA00804B

## Computational methodology

- Code: VASP 6.3.2
- Functional: PBE+U
- Fe Ueff: 4 eV
- Mn Ueff: 5 eV
- Plane-wave cutoff: 550 eV
- Dispersion: Grimme D3, IVDW=11
- Spin-polarized calculations
- Relaxation mesh: Gamma 2x2x1
- Static mesh: Gamma 3x3x2

D3 damping convention remains subject to literature
verification.

## Matched static energy results

| Run | Higher-moment Mn | Energy (eV/cell) |
|---|---|---:|
| Run03 | 22,29,30 | -422.66929102 |
| Run05C | 22,24,29 | -422.40708711 |
| Run06D | 22,24,29 | -422.34722097 |

Relative to Run03:
- Run05C: +14.5669 meV/f.u.
- Run06D: +17.8928 meV/f.u.

Run03 is lowest among these tested configurations.
A global magnetic or structural ground state has
not been established.

## Matched tight-relaxation results

Run05D and Run06E use identical numerical settings:

- EDIFF = 1E-7
- EDIFFG = -0.005 eV/A
- ISIF = 3
- IVDW = 11
- Gamma 2x2x1 mesh

| Property | Run05D | Run06E |
|---|---:|---:|
| Energy (eV/cell) | -422.39325923 | -422.33357056 |
| Maximum force (eV/A) | 0.004062 | 0.003731 |
| Higher-moment Mn | 22,24,29 | 22,24,29 |

Energy difference:

Run06E - Run05D = +0.05968867 eV/cell

Equivalent to +3.3160 meV/f.u.

## Structural comparison

Both configurations retain the same higher-moment
Mn22/24/29 pattern.

Their in-plane lattice distortions differ.

Symmetry-aware matching with pymatgen StructureMatcher:

- Match at site tolerance 0.05: False
- Match at site tolerance 0.10: True
- Normalized RMS distance: 0.03093076
- Normalized maximum distance: 0.09211182

These distances are dimensionless.

The evidence supports reproducibly different
relaxed solutions.

However, separate metastable minima have not
been conclusively demonstrated.

## Electronic differentiation

The reference branch shows three higher-moment
Mn sites with elongated Mn-O octahedra.

These observations support provisional Mn3+-like
and Mn4+-like assignments.

Local magnetic moments and Bader charges are not
formal oxidation-state measurements.

## Outstanding work

1. Dense static calculations on tight geometries
   (proposed Run05E and Run06F).
2. Additional magnetic-ordering tests.
3. Orbital occupation and projected DOS analysis.
4. Literature verification of D3 damping convention.
5. Na extraction and redox analysis.
6. Mg, Al, Si and Ti doping comparisons.
7. P2/O2 stacking and migration studies.

## Data retention

Full calculation files remain on Purdue Anvil.

A verified portable archive was created on
2026-11-12:

parent_p2_benchmark_checkpoint_20261112T164628Z.tar.gz

The archive excludes licensed POTCAR files
and large CHGCAR/WAVECAR data.

Do not publish or redistribute licensed POTCAR data.
