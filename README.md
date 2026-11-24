# P2 Redox Inventory vs Covalency

## Research Title

Redox Inventory or Metal-Oxygen Covalency?
Origins of Dopant-Dependent Stability in Deeply
Desodiated P2-Type Fe-Mn Sodium-Ion Cathodes

## Research Objective

This project investigates the competing roles of
transition-metal redox inventory and metal-oxygen
bonding in determining the high-voltage stability
of P2-type Fe-Mn sodium-ion cathodes.

## Dopant Systems

- Mg2+
- Al3+
- Si4+
- Ti4+

## Research Questions

1. Does transition-metal redox inventory explain
   oxygen stability during desodiation?
2. Does metal-oxygen covalency provide additional
   stabilisation?
3. How does dopant chemistry influence P2/O2
   structural stability?
4. Can Si4+ and Ti4+ distinguish redox effects
   from local bonding effects?

## Computational Methods

- Density Functional Theory
- VASP
- PBE+U
- Grimme D3
- Magnetic structure analysis
- Bader charge analysis
- Electronic density of states
- Selected migration and defect calculations

## Computational Platform

Purdue Anvil HPC

## Repository Structure

- 00_admin: project administration
- 01_literature: literature and research gap
- 02_structures: crystallographic structures
- 03_inputs: VASP input templates
- 04_jobs: job scripts and calculation records
- 05_results: curated results
- 06_analysis: analysis workflows
- 07_figures: research figures
- 08_manuscript: manuscript development
- 09_scripts: reusable computational scripts

## Reproducibility

All tracked calculations should include their
structure, input parameters, software version,
and relevant computational metadata.

Licensed POTCAR files and large raw VASP outputs
are excluded from this repository.

## Status

Project setup and computational benchmarking.


## Verified Parent Benchmark (November 2026)

The 66-atom Na12Fe9Mn9O36 P2 parent benchmark has
completed multiple PBE+U+D3 relaxation, magnetic
configuration and matched-static calculations.

The lowest energy among the tested matched-static
configurations is Run03 (-422.66929102 eV/cell).

Two tight-relaxed Mn22/24/29 branches retain an
energy difference of 59.68867 meV/cell.

These results do not establish a global ground state
or prove distinct metastable minima.

- [Parent benchmark](docs/parent_benchmark.md)
- [Computational methodology](docs/methodology.md)
- [Reproducibility](docs/reproducibility.md)
- [Research references](docs/references.md)
- [Project status](00_admin/PROJECT_STATUS.md)

### Final 3x3x2 tight-geometry statics (2026-11-15)

Run05E: -422.40764591 eV/cell.
Run06F: -422.34836675 eV/cell.

The energy separation is 3.293287 meV/f.u.,
with Run05E lower.

Both retain the Mn22/24/29 higher-moment pattern.

See the [final static benchmark CSV](05_results/parent_benchmark/tight_static_final_2026-11.csv)
and [benchmark interpretation](docs/parent_benchmark.md).

<!-- NA_EXTRACTION_CHECKPOINT_2026_11_24_START -->

## Na-extraction electronic-structure checkpoint (November 2026)

We have evaluated selected Na$_x$Fe$_{0.5}$Mn$_{0.5}$O$_2$ configurations at $x=0.667$, $0.611$ and $0.556$ in an 18-formula-unit P2 supercell. The sampled lowest-energy dense-static Na$_{11}$ configuration is **Vac11** ($E=-418.24829804$ eV per cell). It lies **+7.2139 meV/f.u.** above the tie-line connecting the *sampled* Na$_{12}$ and Na$_{10}$ endpoints. This is **not** a global phase-stability conclusion.

Site-resolved local-moment, Mn–O geometry and projected spin data support a **3 → 2 → 1** Mn$^{3+}$-like-site progression across these selected states. All six Mn22 oxygen ligands decrease in occupied projected O $p$ population for two distinct Na$_{11}$ vacancies, while the wider 36-site response remains vacancy-dependent. Projected orbital occupations are not formal charges or oxygen-hole counts.

- [Na-extraction documentation index](docs/na_extraction/README.md)
- [Matched static energetics](docs/na_extraction/energetics.md)
- [Mn-centered redox](docs/na_extraction/mn_redox.md)
- [Oxygen-ligand response](docs/na_extraction/oxygen_ligand.md)
- [Reproducibility and figure provenance](docs/na_extraction/reproducibility.md)
- [Results and Discussion working draft](08_manuscript/na_extraction_results_draft.md)

<!-- NA_EXTRACTION_CHECKPOINT_2026_11_24_END -->
