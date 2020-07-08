#!/bin/bash

CWD=$(pwd)

N_layers = "3 4 5 6"
vacuum= "40"
input_file=${1:-POSCAR.110}

 for layers in $N_layers; do
     mkdir $layers
     let tetr_layers=$layers-1
     Z=$(echo "2.022912462528*($layers/2-0.1)" | bc -l)
     cat  > temp.tetr << EOF

8
$input_file
M
Ex
0 0
0 0
-$layers 0
Fa
Z
I
$Z
P
C1
3
0 0 $vacuum
y
S
8
POSCAR.${layers}
c

EOF
tetr < temp.tetr
rm temp.tetr
