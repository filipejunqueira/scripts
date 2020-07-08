#!/bin/bash

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

prefix=$1

if [[ ${prefix} == "" ]]; then 
    prefix="OUTCAR*"
fi
# Follow symbolink links
#list_files=$(find -L ./ -name 'OUTCAR') 
# Do NOT follow symbolink links
#list_files=$(find ./ -name 'OUTCAR*') 
#list_files=$(find ./ -name 'OUTCAR.1') 
list_files=$(find ./ -name "${prefix}" ) 

clean_directory

echo "# Total E(eV)  Delta E(eV)    configuration   " 
for i in $list_files; do 

    Energy=$(zgrep -a 'ee  e' $i | tail -n 1 | awk '{print($5)}') 
    path=${i%/*}
    geom_file=${i##*/}
    #geom_file=$(ls $path/${prefix})
    echo  $Energy    ${path}/${geom_file} >> temp_energies_lolo

done

sort -k 1 temp_energies_lolo >> temp_sorted_energies_lolo

minimum_energy=$(tail -n 1 temp_sorted_energies_lolo | awk '{print ($1)}')
energies=($(cat temp_sorted_energies_lolo | awk '{print ($1)}'))
geom_files=($(cat temp_sorted_energies_lolo | awk '{print ($2)}'))
len=${#energies[*]}
let len=$len-1

for i in $(seq 0 $len) ; do
    echo    ${energies[$i]}    $(echo "(${energies[$i]} - $minimum_energy)" | bc)    ${geom_files[$i]}
done

rm temp_sorted_energies_lolo
rm temp_energies_lolo
