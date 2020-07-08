#!/bin/bash

#source activate abienv

CWD=$(pwd)

ecut= "60"

kpoints= "4 6 8 10 12 14 16 18 20"

for i in $kpoints; do 
   dir=kpoints_$i
   mkdir $dir
   #cp GaAs.files As.GGA_PBE-JTH.xml Ga.GGA_PBE-JTH.xml $dir
   cp GaAs.files $dir
   cd $dir
   cat > GaAs_abinit.in << EOF

# GaAs
# abinit input buchered by Filipe based on the NaCl example
# basis set, bands, k-points, SCF tolerance

ecut $i

# pawecutdg = PAW - Energy CUToff for the Double Grid. Define the energy cut-off for the fine FFT grid (the “double grid”, that allows one to transfer data from the normal, coarse, FFT grid to the spherical grid around each atom). Pawecutdg must be larger or equal to ecut. If it is equal to it, then no fine grid is used. Should use 30 for calculations with high accuracy. 

pawecutdg 100

# occcopt is a ocupation option. 1 gives a semiconductor.
occopt 1

# temperature of smearing. 
tsmear 0.01

# Number of grid points for K Points generation.
ngkpt $kpoints $kpoints $kpoints

# Number of shifts for K point grids, max is 8. 
nshiftk 1

# Shifts for K point grids. Does not need to be defined if nshiftk is equal to 1. 
shiftk
   0 0 0

# Tolerance of Diference of total Energy (stops when the absolute diference reaches this value twice).
toldfe 1e-10

# unit cell values of which primitive translations rprim should be multiplied. Given in Bohr units by default. Converted from David's CONTCAR file with abistruct.py convert FILENAME -f abivars.

acell    1.0    1.0    1.0
xred
    0.0000000000    0.0000000000    0.0000000000
    0.2500000000    0.2500000000    0.2500000000
rprim
    0.0000000000    5.4488117437    5.4488117437
    5.4488117437    0.0000000000    5.4488117437
    5.4488117437    5.4488117437    0.0000000000
 
typat 1 2
natom 2
ntypat 2
znucl 31 33

# Geometrical relaxation

# ionmov = Ionic Moves: 0 = Ions do not mov. 
ionmov 0

# molecular dynamics time steps size if ionmov is not 0.
ntime 10

# tolerance on the Maximal Force where the relaxation iterations stop.
tolmxf 0.00005

# lattice dilatation: Max value (default is 1). 
dilatmx 1.05000

# Energy cutoff smearing. Recomended value is 0.5
ecutsm 0.50000

# Other stuff - no idea what that is...
# prtcml 1

EOF

abinit < GaAs.files > log
cd $CWD

done
