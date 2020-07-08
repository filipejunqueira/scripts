#!/bin/bash

CWD=$(pwd)

N_layers="3 4 5 6 7 8"
vacuum="40"
input_file=${1:-POSCAR.110}

for layers in $N_layers; do
     dir=nlayers_${layers}   
     mkdir $dir
     let tetr_layers=-$layers+1
     Z=$(echo "2.022912462528*($layers/2-0.1)" | bc -l)
     cat  > temp.tetr << EOF

8
$input_file
M
Ex
0 0
0 0
$tetr_layers 0
Fa 
Z
I
$Z
Cr
P
C1
3
0 0 $vacuum
y
S
8
POSCAR.${layers}_layers
c
Q
Q
Q

EOF
tetr < temp.tetr
rm temp.tet

tetr < temp_tetr 2&> /dev/null
mv POSCAR.${layers}_layers ${dir}/POSCAR
#cp INCAR KPOINTS POTCAR geom.xyz ${dir}
cp geom.xyz ${dir}

done
