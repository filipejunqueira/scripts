#!/bin/bash

# Compress  and after removes all the $PREFIX* files bigger than $SIZE found recursively
# from the CWD (Current Work Directory). The files are compressed in their local path. 

# The aim of this script is to save space in the SSD (more than 4 times the
# size of the files)
# NOTE: 
#   - Vim can open directly .tar.gz files
#   - zgrep -a 'string' file.tar.gz searchs for the string in the compressed files

CWD=$(pwd)
SIZE=200k    #!> Adjust this value to your desired size
#               `b'    for 512-byte blocks (this is the default if no suffix is used)
#               `c'    for bytes
#               `w'    for two-byte words
#               `k'    for Kilobytes (units of 1024 bytes)
#               `M'    for Megabytes (units of 1048576 bytes)
#               `G'    for Gigabytes (units of 1073741824 bytes)
# 
PREFIX=$1

# Find files with a size bigger than $SIZE MB which will be compressed
# Exlcudes the files already compressed
# string=${1}*.out
string=${1}*
find ./ -name "${string}" -size +${SIZE}  | grep -v .tar.gz > tmpFiles

for i in $(cat tmpFiles); do 

   # Extract the path_to_i removing the file's name (all after the last /)
   PATH_TO_i=${i%/*}
   # Gets the filename from the path $i removing the "${PATH_TO_i}/" string
   filename=${i/${PATH_TO_i}\//}

   echo "Compressing $i --> $i.tar.gz"
   cd $PATH_TO_i
   tar czf ${filename}.tar.gz $filename
   # If compression ends succesfully
   if [ $? == 0 ]; then 
      rm $filename
   else 
      echo WARNING: File can not be compressed: $i 
   fi
   cd $CWD

done
rm tmpFiles
