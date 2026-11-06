# P2 Parent Benchmark: Na12Fe9Mn9O36

DFT relaxation, magnetism, Jahn–Teller distortion and Bader analysis for the first P2 parent structure.

**Date:** 2026-11-06 | **Platform:** Purdue Anvil | **Code:** VASP 6.3.2

## Summary

I relaxed a 66-atom P2 supercell (Na12Fe9Mn9O36, normalized Na0.667Fe0.5Mn0.5O2) with PBE+U+D3, then ran a denser static calculation and a Bader analysis on it.

Three Mn sites (22, 29, 30) stand out from the other six (23–28): they have higher magnetic moments, strongly elongated MnO6 octahedra, and lower Bader charges. This points to **3 Mn3+-like and 6 Mn4+-like sites**, which matches the nominal charge balance (average Mn of +3.667). This is a provisional assignment, not a formal oxidation-state result.

This is one ferromagnetic-initialized solution only. It is not a confirmed magnetic ground state.

## Setup

- Starting structure: `POSCAR_f4e8_0` (pymatgen + Ewald annealing, seed 7, Na_f:Na_e = 4:8)
- PBE, PAW (Na_pv, Fe_pv, Mn_pv, O), ENCUT 550 eV, spin-polarized
- DFT+U (Dudarev): U(Fe) = 4 eV, U(Mn) = 5 eV
- Dispersion: D3 zero damping (`IVDW = 11`), provisional choice
- Initial magnetic state: ferromagnetic

| Run | Job ID | What | k-mesh | Final energy (eV) |
|---|---|---|---|---|
| 01 | 21960601 | Fixed-cell PBE+U relaxation | 2×2×1 | -411.00792 |
| 02 | 21977409 | Variable-cell PBE+U+D3 relaxation (ISIF 3) | 2×2×1 | -422.63844 |
| 03 | 21997249 | Static PBE+U+D3 on Run 02 geometry | 3×3×2 | -422.66929 |

Run 01 is not energy-comparable to Run 02 (no D3, fixed cell). Run 02 converged to a max force of 0.0096 eV/Å with all stress components below 0.29 kbar.

## Relaxed cell (Run 02)

| Quantity | Value |
|---|---|
| Vector lengths | 8.857, 8.947, 11.185 Å |
| In-plane (÷3) | 2.952, 2.982 Å |
| Volume | 769.21 Å³ (42.73 Å³/f.u.) |

Compared with the rough experimental reference (a ≈ 2.94 Å, c ≈ 11.20 Å), in-plane lengths are about 0.4% and 1.4% larger and c is about 0.1% smaller. The reference is approximate and should be checked before publication. Since the two in-plane lengths differ, don't quote a single hexagonal *a* without a caveat.

## Magnetic moments (Run 02, LORBIT = 11)

- Fe (9 sites): all about 4.23 μB
- Mn 22, 29, 30: mean 3.93 μB
- Mn 23–28: mean 3.31 μB
- Total cell moment: 75 μB

The higher-moment Mn sites ended up as 22, 29, 30, although the initial guess was 22–24. So the solution is sensitive to initialization.

## Mn–O coordination

| Group | Mean Mn–O (Å) | Mean distortion index |
|---|---|---|
| Mn 22, 29, 30 | 2.056 | 0.047 |
| Mn 23–28 | 1.954 | 0.008 |

Each of the three distorted sites has two long Mn–O bonds (about 2.18–2.22 Å) lying almost opposite each other (mean angle 175°). That is a two-long/four-short elongation, consistent with high-spin d4 Mn3+.

## Bader analysis (Run 03)

All 66 atoms were found, and the total integrated population is 543.000 e, matching the expected valence count. Net charge = ZVAL − Bader electrons.

| Species | Mean net charge (e) |
|---|---|
| Na | +0.864 |
| Fe | +1.768 |
| Mn | +1.804 |
| O | -1.181 |

Mn 22, 29, 30 average +1.712 e versus +1.850 e for Mn 23–28, a difference of about 0.14 e. This supports the electronic differentiation, but Bader charges are not formal oxidation states.

## Limitations

1. Only one FM-initialized solution has been compared; no other Mn3+ site arrangements or magnetic orderings yet.
2. D3 zero vs BJ damping is unresolved against the reference method.
3. The preliminary band-edge numbers (about 0.89 eV spin-up, 2.56 eV spin-down) still need a DOS cross-check and k-point convergence.
4. The three Jahn–Teller axes have not been compared in a common crystallographic frame.
5. PDOS (Mn/Fe 3d, O 2p) and charge-density difference are still to do.

## Next steps

- Run at least three different Mn3+ site triplets with identical settings
- Compare magnetic configurations and find the lowest-energy parent
- Spin-resolved and orbital-projected DOS
- Then move to doped structures (Mg, Al, Si, Ti) and P2/O2 crossover models

## Files

Compact CSVs (run summary, magnetic moments, Mn–O coordination, lattice parameters, Bader charges and summaries) and `POTCAR_provenance.md` sit alongside this report. Raw VASP outputs stay on Anvil under `04_jobs/benchmark/parent_p2_x067/`. Do not commit POTCAR, WAVECAR, CHGCAR or AECCAR files.

## Reference

Chakraborty, House and Islam, *J. Mater. Chem. A* (2025), [10.1039/D5TA00804B](https://doi.org/10.1039/D5TA00804B). Used as a methods and materials reference only. Its Table 1 values are r2SCAN, so they are not PBE+U+D3 comparisons.
