# Computational Methodology

## Research system

P2-type Na0.667Fe0.5Mn0.5O2 layered sodium-ion cathode.

Parent simulation cell:
- Na12Fe9Mn9O36
- 66 atoms
- 18 formula units

## Software

- VASP 6.3.2
- Purdue Anvil HPC
- Python, ASE, pymatgen and spglib for structure analysis

## Electronic structure

- Exchange-correlation: PBE
- PAW potentials: Na_pv, Fe_pv, Mn_pv, O
- Plane-wave cutoff: 550 eV
- Spin polarization: ISPIN = 2
- Dudarev DFT+U
- Fe Ueff = 4 eV
- Mn Ueff = 5 eV
- LASPH = True
- LMAXMIX = 4

## Dispersion

Variable-cell benchmark calculations use IVDW = 11,
corresponding to Grimme D3 zero damping.

The precise damping convention of the literature
reference must be verified before claiming an
identical computational methodology.

## Geometry optimization

Main variable-cell relaxations:
- Gamma-centered 2x2x1 k-point mesh
- IBRION = 2
- ISIF = 3
- EDIFF = 1E-6
- EDIFFG = -0.01 eV/A

Tighter comparison calculations (Run05D, Run06E):
- EDIFF = 1E-7
- EDIFFG = -0.005 eV/A
- Gamma-centered 2x2x1 mesh

## Static calculations

Reference static calculations:
- Gamma-centered 3x3x2 k-point mesh
- EDIFF = 1E-7
- NSW = 0
- IBRION = -1

Run03, Run05C and Run06D follow matched static settings.

Final dense static calculations on the tighter
Run05D and Run06E geometries remain pending.

## Magnetic and structural analysis

Multiple Mn magnetic initializations and controlled
Jahn-Teller oxygen displacements were tested.

The higher-moment Mn populations are consistent with
provisional Mn3+-like assignments.

Magnetic moments and Bader charges must not be
interpreted directly as formal oxidation states.

## Limitations

- A global magnetic ground state is not established.
- Distinct metastable minima are not yet proven.
- Oxygen redox has not yet been demonstrated.
- Dopant and desodiation comparisons remain pending.
