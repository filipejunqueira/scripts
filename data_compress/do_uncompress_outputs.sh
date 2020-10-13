#!/bin/bash

CWD=$(pwd)
prefix=$1 
string=${1}*.tar.gz

find ./ -name "${string}"  > tmpTarFiles

for i in $(cat tmpTarFiles); do 
   # Extract the path_to_i removing the file's name (all after the last /)
   PATH_TO_i=${i%/*}
   # Gets the filename from the path $i removing the "${PATH_TO_i}/" string
   filename=${i/${PATH_TO_i}\//}

   cd $PATH_TO_i
   outputfile=$(tar xzvf ${filename})
   echo "Uncompressing: $i --> $PATH_TO_i/$outputfile"
   if [ $? == 0 ]; then 
      rm ${filename}
   else 
      echo WARNING: File can not be uncompressed: $i 
   fi
   cd $CWD
done
rm tmpTarFiles
