# Site-resolved oxygen-ligand response

Occupied site-projected O p populations were integrated to the Fermi level of each calculation. The 36 physical oxygen sites were tracked by parent-structure indices, using the verified non-Na index shift after Na removal.

The six parent oxygen atoms around Mn22 are **O31, O32, O37, O50, O55, O56**. This coordination shell is preserved as 6/6 nearest oxygen neighbors in Na12, Na11 Vac11 and Na11 Vac01.

## Mn22 O6 response relative to Na12

| Descriptor | Vac11 | Vac01 |
|---|---:|---:|
| Signed Mn22 O6 O p projection change | **-0.077563** | **-0.065479** |
| Negative-response Mn22 oxygen sites | **6/6** | **6/6** |
| Whole-cell signed O p change (36 sites) | -0.110102 | -0.109502 |
| Mn22 O6 share of sum of absolute site changes | **35.80%** | **36.37%** |
| Mean per-site absolute response enrichment vs other 30 O | **2.788×** | **2.858×** |

The six Mn22 O atoms are **16.7% of the oxygen sites** but contribute ~36% of the sum of absolute O-site projected population changes. This is a *spatial-response concentration* metric, **not** a fraction of redox charge.

For Vac11 the vacancy-nearest six O sites overlap the parent Mn22 shell at 2 of 6 sites; for Vac01 the nearest shell overlap is 0 of 6. The robust Mn22-shell response thus cannot be explained solely by membership among the nearest six O atoms to the vacancy, although longer-range relaxation and electrostatic effects remain possible.

## Different vacancy ordering, different local response

The complete 36-site Vac11 and Vac01 difference vectors (relative to the same parent) have **Pearson r = +0.62722**, with matching change signs at **23/36** sites. The whole-cell projected O p populations are almost equal (124.014355 and 124.014955 respectively), but the **sum of absolute sitewise differences** is **0.158823** projected electrons.

For example parent O55 shows -0.018656 (Vac11) versus -0.005315 (Vac01). The Mn30 O6 signed change is +0.025685 (Vac11) compared with +0.000973 (Vac01), even as Mn30 remains Mn3+-like at Na11 in both arrangements.

Because the mean response integrates differently for each geometry, these differences indicate vacancy-sensitive *projected orbital redistribution*, not experimentally resolved charge transfer or oxygen oxidation.

## Scientific limitations

- Atomic/orbital projections depend on the VASP representation and are not formal Bader charges, quantitative oxygen holes or a stand-alone covalency measure.
- Each structure is referenced to its own Fermi energy; composition-to-composition DOS traces do not provide absolute band-edge offsets.
- The parent and two Na11 vacancy arrangements are different relaxed geometries.
- Some individual site-sign differences are small; magnitude and numerical convergence matter.

[Figure C](figures.md) · [Curated summary CSV](../../05_results/na_extraction/oxygen_response_summary.csv)
