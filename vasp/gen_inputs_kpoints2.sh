#!/bin/bash

CWD=$(pwd)
source activate abienv

ecut="20 "
kpoints=" 4 6 8 10 12 14 16 18 20"

for i in $kpoints; do 
   dir=kpoints_$i
   mkdir $dir
   cp au.files Au.GGA_PBE-JTH.xml $dir
   cd $dir
   cat > au.in << EOF
ecut $ecut
pawecutdg  100
occopt 4
tsmear 0.005
ngkpt $i $i $i
nshiftk 1
shiftk 
0 0 0
toldfe 1e-10

ionmov 0
# Structural parameters
acell    3*7.70677546732  

rprim    0.000000000000000   0.500000000000000   0.500000000000000 
         0.500000000000000   0.000000000000000   0.500000000000000 
         0.500000000000000   0.500000000000000   0.000000000000000 
       
natom    1  
ntypat   1  
typat    1  
znucl    79  
xred     0.000000000000000   0.000000000000000   0.000000000000000 
EOF

abinit < au.files > log
cd $CWD

done

