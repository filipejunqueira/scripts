#!/bin/bash

CWD=$(pwd)

input_file=${1:-POSCAR.110}
8
$input_file
M
An
An
Aa
#atom Chemical element Species
Ga
#Atom position
0.00000   1.43042   9.56874
S
8
POSCAR.Add
c
Q
Q
Q

EOF
tetr < temp.tetr
rm temp.tetr

tetr < temp_tetr 2&> /dev/null
#mv POSCAR.${layers}_layers ${dir}/POSCAR
#cp INCAR KPOINTS POTCAR geom.xyz ${dir}
#cp geom.xyz ${dir}

done
