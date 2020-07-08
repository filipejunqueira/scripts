#!/bin/bash

# Returns the path in the remote server
# TODO: If the CWD is $HOME or upper the path will be wrong
CWD=$(pwd)
GRAVITY_PATH="/mnt/scratch/users/k_filipe"
THOMAS_PATH="/home/mmm0540"
BACKUP_PATH="/mnt/localbackup/david"
LOCAL_PATH=$HOME

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
elif [ $1 == 'backup' ]; then 
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=${BACKUP_PATH}$TEMP/
else 
   echo Sorry, server not known
   echo try one of the followings:
   echo - gravity
   echo - thomas
   echo - backup
   exit 1
fi

echo  $REMOTE_PATH
