# Mn-centered formal-redox fingerprints

The selected Na12 parent, Na11 Vac11 and Na10 CL-far structures exhibit **3 → 2 → 1 Mn3+-like centers** based jointly on site-local moments, coordination and projected spin polarization.

| Parent Mn | Na12 | Na11 Vac11 | Na10 CL-far |
|---|---|---|---|
| Mn22 | Mn3+-like | **Mn4+-like** | Mn4+-like |
| Mn29 | Mn3+-like | Mn3+-like | Mn3+-like (spin reversed) |
| Mn30 | Mn3+-like | Mn3+-like | **Mn4+-like** |

## Occupied Mn d spin polarizations

$P_d=N_{d,\uparrow}-N_{d,\downarrow}$, in projected-electron units:

| Parent Mn | Na12 | Na11 Vac11 | Na10 CL-far |
|---|---:|---:|---:|
| Mn22 | +3.85814 | +3.26422 | +3.25342 |
| Mn29 | +3.87565 | +3.86222 | **-3.81907** |
| Mn30 | +3.85819 | +3.85024 | +3.23370 |

The primary drop in $|P_d|$ occurs at Mn22 in the first interval and Mn30 in the second. Parent Mn29 **reverses spin** at Na10 but retains a large polarization magnitude. A signed change is not automatically an oxidation-state change.

In Na11 Vac11, Mn22 has moment +3.333 μB, mean Mn–O distance 1.9522 Å and distortion index 0.000015; Mn29 has +3.930 μB, 2.0528 Å and 0.002549; Mn30 has +3.918 μB, 2.0492 Å and 0.002444. These structural signatures support the oxidation-state fingerprint.

## VASPKIT–pymatgen cross-parser validation

VASPKIT Standard Edition 1.5.1 and pymatgen integrated **the same underlying VASP DOS data** for all nine Mn sites. All nine signed-polarization results agree within an absolute difference of **0.00020 projected electrons**. That is a strong check of atom indices, five d-orbital summation, sign conventions and numerical integration, but **not** independent verification of a DFT functional or true magnetic global ground state.

[Full nine-row numerical comparison](../../05_results/na_extraction/mn_d_crossparser_validation.csv) · [Figure A and B](figures.md)

The selected Na11 Vac11 and Na10 CL-far structures are **not nested vacancy-removal states**; dashed lines in figures are guides between separately sampled compositions, not evidence of an actual continuous pathway.
