#!/bin/bash

# List all the CONTCAR.* in the folder and rearranges them (ONLY FOR
# VISUALIZATION) wrt to the POSCAR.1 (initial geometry) Using tetr.
# Writes evolution.xyz but does nothing to the CONTCARs

files=$(ls -v CONTCAR.*)

if [ -f evolution.xyz ]; then
     rm evolution.xyz
fi
# if ! [ -f POSCAR.1 ]; then
#    POSCAR="../POSCAR.1"
# else
#    POSCAR="POSCAR.1"
# fi

# if ! [ -f POSCAR.0 ]; then
#    POSCAR="../POSCAR.0"
# else
#    POSCAR="POSCAR.0"
# fi

if [ -f POSCAR.0 ]; then
    POSCAR="POSCAR.0"
elif [ -f ../POSCAR.0 ]; then
    POSCAR="../POSCAR.0"
elif [ -f POSCAR.1 ]; then
    POSCAR="POSCAR.1"
elif [ -f ../POSCAR.1 ]; then
    POSCAR="../POSCAR.1"
fi

for file in $files; do
     cat > temp.tetr << EOF
8
$file
M
Rf
8
$POSCAR
W
Q
Q
EOF
     tetr < temp.tetr 2&> /dev/null
     #tetr < temp.tetr
     cat geom.xyz >> evolution.xyz
done
