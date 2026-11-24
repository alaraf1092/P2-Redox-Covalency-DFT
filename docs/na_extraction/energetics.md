# Matched static energetics and limited tie-line test

## Sampled lowest energies at each selected composition

| Structure | Composition | Energy (eV / 18-f.u. cell) | EIGENVAL gap (eV) | Mn3+-like parent sites |
|---|---:|---:|---:|---|
| Parent `run03` | Na12, $x=0.667$ | -422.66929102 | 0.8853 | 22, 29, 30 |
| Vac11 | Na11, $x=0.611$ | **-418.24829804** | 0.4249 | 29, 30 |
| CL-farthest Na01/Na04 | Na10, $x=0.556$ | -414.08700598 | 1.0146 | 29 |

All energies above are from matched **Γ-centered 3×3×2 PBE+U+D3** statics. Energies from 2×2×1 ionic relaxations must **not** be mixed into this ranking or tie-line analysis.

## Na11 single-vacancy ranking

| Rank | Vacancy | Dense-static energy (eV/cell) | Relative to Vac11 (meV/f.u.) | Above sampled tie line (meV/f.u.) |
|---:|---|---:|---:|---:|
| 1 | **Vac11** | **-418.24829804** | 0.000 | **+7.2139** |
| 2 | Vac03 | -418.23008823 | +1.012 | +8.2256 |
| 3 | Vac05 | -418.18044974 | +3.769 | +10.9833 |
| 4 | Vac01 | -417.96101912 | +15.960 | +23.1739 |
| 5 | Vac04 | -417.91088995 | +18.745 | +25.9588 |

There are six converged ionic relaxations in the sampled Na11 set; **Vac08 lacks a matched dense static**. The remaining six single-vacancy sites were not sampled in this checkpoint. A smaller energy is better for this fixed-composition matched static comparison; the small ~1 meV/f.u. Vac11–Vac03 splitting warrants k-mesh and magnetic-seed sensitivity checks.

## Selected-endpoint tie line

For the Na11 midpoint between the sampled Na12 and Na10 cells:

$$
E_\mathrm{tie}=\tfrac12(E_{\mathrm{Na12}}+E_{\mathrm{Na10}})
=-418.37814850\;\mathrm{eV/cell}.
$$

$$
\Delta E_{\mathrm{Vac11}}=E_{\mathrm{Vac11}}-E_\mathrm{tie}
=+0.12985046\;\mathrm{eV/cell}
=+7.2139\;\mathrm{meV/f.u.}.
$$

This compares **selected zero-temperature internal energies** only. A positive sampled excess is **not proof** that all Na11 arrangements are unstable or that the equilibrium phase diagram exhibits phase separation; additional vacancies, magnetic/electronic states, convergence and finite-temperature free energies remain unresolved.

[Machine-readable energy table](../../05_results/na_extraction/na11_dense_static_energies.csv)
