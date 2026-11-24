# Reproducibility and provenance — Na extraction

## Source directories (relative to research project root)

These are **relative paths**, not instructions to clone raw VASP calculations into GitHub:

| State | Relative VASP static directory |
|---|---|
| Na12 parent | `04_jobs/benchmark/parent_p2_x067/run03_static_pbeu_d3zero_3x3x2/` |
| Na11 Vac11 | `04_jobs/na_extraction/x0611_single_vacancies/Na11_Vac11/static_pbeu_d3zero_3x3x2/` |
| Na11 Vac03 | `04_jobs/na_extraction/x0611_single_vacancies/Na11_Vac03/static_pbeu_d3zero_3x3x2/` |
| Na11 Vac05 | `04_jobs/na_extraction/x0611_single_vacancies/Na11_Vac05/static_pbeu_d3zero_3x3x2/` |
| Na11 Vac01 | `04_jobs/na_extraction/x0611_single_vacancies/Na11_Vac01/static_pbeu_d3zero_3x3x2/` |
| Na11 Vac04 | `04_jobs/na_extraction/x0611_single_vacancies/Na11_Vac04/static_pbeu_d3zero_3x3x2/` |
| Na10 CL-far | `04_jobs/na_extraction/x0556_geometric_six/CL_farthest_Na01_Na04/static_pbeu_d3zero_3x3x2/` |

## Validation sequence

1. Completed Slurm jobs confirmed with zero process exit codes and VASP completion footer; convergence separately checked using `Vasprun.converged_electronic`.
2. Band gaps from `Eigenval(occu_tol=1e-3)`; do not substitute pymatgen's different default occupancy threshold.
3. Local moments, Mn–O distances and Jahn–Teller-like distortions used as *formal-valence fingerprints*.
4. Mn projected d spin occupations summed over five d orbitals and integrated to each calculation's Fermi level.
5. VASPKIT **1.5.1** task `112` with `INCAR`, `POSCAR`, `DOSCAR`, **`PROCAR`**, `OUTCAR` present in a separate working directory, selecting the correct **current POSCAR atom index**. VASPKIT writes a negative spin-down integral in its `IPDOS_*_DW.dat` plotting convention.
6. Nine Mn sites agreed between VASPKIT and pymatgen to within 0.00020 projected electrons in signed d polarization. Both parsers share a **common** VASP source.
7. O p occupations calculated via pymatgen's `CompleteDos.get_site_spd_dos` and integrated to each state's $E_F$; parent O6 identity validated 6/6 across Na12, Na11 Vac11, Na11 Vac01.

## Figure and numerical source locations

| Figure | Research-storage relative directory |
|---|---|
| A and B (corrected v2) | `05_analysis/figures/Na_extraction_VASPKIT_PDOS_v2/` |
| C (oxygen v1) | `05_analysis/figures/Na_extraction_O_response_v1/` |
| VASPKIT–pymatgen numeric CSV | `05_analysis/figures/Na_extraction_VASPKIT_PDOS_v1/VASPKIT_pymatgen_validation.csv` |
| Full 36-O site CSV | `05_analysis/figures/Na_extraction_O_response_v1/O36_site_resolved_changes.csv` |
| O-response generating script | `05_analysis/figures/Na_extraction_O_response_v1/generate_oxygen_figure.py` |
| O-response provenance text | `05_analysis/figures/Na_extraction_O_response_v1/README_analysis.txt` |

The repo contains **curated numeric tables and PNG previews**; these are not substitutes for the full research-storage record or licensed PAW data.

## Information never to commit

Never commit licensed `POTCAR` content, `WAVECAR`, `CHGCAR`, `PROCAR`, `DOSCAR`, `OUTCAR`, `vasprun.xml`, `AECCAR` files, user credentials, SSH keys, private scheduler logs or whole raw output trees. Review all `git add` and `git status` results before pushing a public repository.

## Source dataset notes

- Na11 Vac11 is the lowest **sampled** dense-static candidate, not a verified global ground state.
- The Na11 Vac11 and Na10 CL-far structures are not nested vacancy-removal configurations.
- Orbital projections are not formal oxidation charges.
- `PDOS_A21_*` from Na11 Vac11 maps to physical parent Mn22 (atom-index shift -1).
