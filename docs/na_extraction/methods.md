# Computational methods — Na extraction

## Models

- P2 layered Na$_x$Fe$_{0.5}$Mn$_{0.5}$O$_2$; 18 formula units per computational cell.
- Na12Fe9Mn9O36: 66 atoms, $x=12/18=0.6667$.
- Na11Fe9Mn9O36: 65 atoms, $x=11/18=0.6111$.
- Na10Fe9Mn9O36: 64 atoms, $x=10/18=0.5556$.
- The candidate set is limited to configurations explicitly sampled and electronically/ionically validated. No exhaustive Na ordering or magnetic search is asserted.

## DFT settings

| Parameter | Setting |
|---|---|
| Code | VASP 6.3.2 |
| Exchange–correlation | PBE |
| Hubbard correction | Dudarev PBE+U, Fe $U_\mathrm{eff}=4$ eV; Mn $U_\mathrm{eff}=5$ eV |
| Dispersion | Grimme D3 zero damping, `IVDW = 11` |
| PAW species sequence | `Na_pv Fe_pv Mn_pv O` |
| POTCAR identity | SHA256 `ec5f472bb65c08ad4e51ffbbfb03a2b056f3b738b3d6300b117a01b29c1bba3d` (hash only; **licensed content is not tracked**) |
| Plane-wave cutoff | `ENCUT = 550 eV` |
| Spin and non-spherical corrections | `ISPIN = 2`, `LASPH = .TRUE.`, `LMAXMIX = 4` |
| Ionic relaxation | Γ-centered 2×2×1, `IBRION = 2`, `ISIF = 3`, `EDIFF = 1e-6`, `EDIFFG = -0.01 eV/Å` |
| Matched dense static | Γ-centered 3×3×2, `NSW = 0`, `IBRION = -1`, `LORBIT = 11`, `NEDOS = 3000` |

For the complete current INCAR and run-specific controls, consult original VASP input files on institutionally managed research storage; this repository is a curated, non-raw-data record.

## Parent-index mapping

Original Na12 POSCAR indices: Na1–12, Fe13–21, Mn22–30, O31–66. The studied extraction permutations remove Na sites, causing the following shifts in **non-Na** atom indices:

| Physical site in parent | Na12 | Na11 | Na10 |
|---|---:|---:|---:|
| Parent Mn22 | 22 | 21 | 20 |
| Parent Mn29 | 29 | 28 | 27 |
| Parent Mn30 | 30 | 29 | 28 |

The retained atom-order mapping and nearest-neighbor shells were checked against the relaxed structures. Recompute if atom order is modified.

## Local Mn fingerprints

The phrase **Mn3+-like** describes a combined signature of high local moment (about 3.9 μB), longer/distorted Mn–O shell (about 2.05 Å) and projected spin behavior. **Mn4+-like** describes the contrasting ~3.3 μB, shorter/~1.95 Å shell. This is a formal-state *fingerprint*, not a uniquely measured oxidation charge.

Occupied DOS projected occupations are integrated to each calculation's own Fermi energy. Electronic gaps were extracted with `Eigenval(occu_tol=1e-3)`. All three selected endpoint/intermediate statics passed electronic-convergence and output-footer audits.
