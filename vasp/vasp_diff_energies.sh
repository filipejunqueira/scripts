#!/bin/bash

# ----------------------------------------------------------------------
# Script util para calcular facilmente energias de enlace.
# Busca todos los OUTCAR con nombre <prefix> (Argumento 1). 
# - Extrae sus energias y les resta la energia del archivo de referencia
#   <REF_FILE> (Argumento 2)
#
# Usage:
#     vasp_diff_energies OUTCAR /path/to/reference/OUTCAR
#       - Solo usara los ficheros OUTCAR que encuentre
# or 
#     vasp_diff_energies OUTCAR.1 /path/to/reference/OUTCAR
#       - Solo usara los ficheros OUTCAR.1 que encuentre
#
# OUTPUT:
#  - Prints the result in the terminal
# ----------------------------------------------------------------------

function clean_directory {
# Clean the temporay files just in case
if [ -f temp_energies_lolo ]; then
    rm temp_energies_lolo
fi
if [ -f temp_sorted_energies_lolo ]; then
    rm temp_sorted_energies_lolo
fi
}

CWD=$(pwd)


ARGC=$#
ARG_REQUIRED=2

if [ $ARGC -ne $ARG_REQUIRED ]; then 
    echo "Required arguments: 2"
    echo "  Arg 1: Prefix for the outcars"
    echo "  Arg 2: Path of the Reference file" 
    exit 1
fi

prefix=$1
REF_FILE=$2

# Follow symbolink links
#list_files=$(find -L ./ -name 'OUTCAR') 
# Do NOT follow symbolink links
list_files=$(find ./ -name "${prefix}" ) 

clean_directory

echo "# Total E(eV)  Delta E(eV)    configuration   " 
for i in $list_files; do 

    minimum_energy=$(zgrep -a 'ee  e' $REF_FILE | tail -n 1 | awk '{print($5)}')
    Energy=$(zgrep -a 'ee  e' $i | tail -n 1 | awk '{print($5)}') 
    path=${i%/*}
    geom_file=${i##*/}
    #geom_file=$(ls $path/${prefix})
    echo  $Energy    ${path}/${geom_file} >> temp_energies_lolo

done

sort -k 1 temp_energies_lolo >> temp_sorted_energies_lolo

energies=($(cat temp_sorted_energies_lolo | awk '{print ($1)}'))
geom_files=($(cat temp_sorted_energies_lolo | awk '{print ($2)}'))
len=${#energies[*]}
let len=$len-1

for i in $(seq 0 $len) ; do
    echo    ${energies[$i]}    $(echo "(${energies[$i]} - $minimum_energy)" | bc)    ${geom_files[$i]}
done

rm temp_sorted_energies_lolo
rm temp_energies_lolo
