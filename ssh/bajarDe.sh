#!/bin/bash

CWD=$(pwd)
GRAVITY_PATH="/mnt/scratch/users/k1472185/"
THOMAS_PATH="/home/mmm0540/"
LOCAL_PATH=$HOME

EXCLUDE_FILE=${LOCAL_PATH}/scripts/ssh/exclude_files.dat
EXTRA_OPT=$2

if [[ $1 == "" ]]; then  
    echo "Please, choose a remote server"
    exit 1
fi
# work out the paths
if [ $1 == 'gravity' ]; then 
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=gravity:${GRAVITY_PATH}$TEMP/
elif [ $1 == 'thomas' ]; then 
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=thomas:${THOMAS_PATH}$TEMP/
else 
   echo Sorry, server not known
   echo "  - gravity"
   echo "  - thomas"
   exit 1
fi

echo Gathering files from: $REMOTE_PATH
rsync -auvz $EXTRA_OPT --exclude-from=${EXCLUDE_FILE} ${REMOTE_PATH} ${CWD}/
echo 
echo Remote path: $REMOTE_PATH
