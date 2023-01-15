#!/bin/bash
#
# Will upload the current folder (in $PWD) to the remote server. If the remote path does not exist, it will create it on the server.
# To download the folder use the alternative script 'bajarDe'
# Usage:
# 
#     upload_to <cluster_name> ("optional extra options")


function work_out_remote_dir {
CLUSTER=$1
REMOTE_DIRECTORY=$2

# Checking if remote directory exists
if (ssh -q $CLUSTER "! [ -d $REMOTE_DIRECTORY ]") ; then
    # If does not exist, then create path
    echo Remote directory does not exists. Creating directory...
    ssh -q $CLUSTER " mkdir -p $REMOTE_DIRECTORY "
fi
}

# PATHS
CWD=$(pwd)
GRAVITY_PATH="/mnt/scratch/users/k_filipe/"
THOMAS_PATH="/home/mmm0540"
YOUNG_PATH="/home/mmm0792"
AUGUSTA_PATH="/home/ppzfl"
LOCAL_PATH=$HOME

# List of files excluded to be uploaded/downloaded
EXCLUDE_FILE=$HOME/scripts/ssh/exclude_files.dat

CLUSTER=$1
EXTRA_OPT=$2
if [[ $CLUSTER == "" ]]; then  
    echo "Please, choose a remote server:"
    echo "  - gravity"
    echo "  - thomas"
    echo "  - young"
    echo "  - augusta"
    exit 1
fi

# work out the paths
if [ $CLUSTER == 'gravity' ]; then 
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=${GRAVITY_PATH}$TEMP/
elif [ $CLUSTER == 'thomas' ]; then 
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=${THOMAS_PATH}$TEMP/
elif [ $CLUSTER == 'augusta' ]; then
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=${AUGUSTA_PATH}$TEMP/
elif [ $CLUSTER == 'young' ]; then 
   TEMP=${CWD/$LOCAL_PATH/}
   REMOTE_PATH=${YOUNG_PATH}$TEMP/
else 
   echo Sorry, server not known. Choose between:
   echo "  - gravity"
   echo "  - thomas"
   echo "  - young"
   echo "  - augusta"
   exit 1
fi

# If remote path does not exist, create the path
echo CLUSTER: $CLUSTER
echo REMOTE PATH: $REMOTE_PATH
work_out_remote_dir $CLUSTER $REMOTE_PATH

echo Uploading files to: $CLUSTER:$REMOTE_PATH
echo "Are you sure you want to do this [Y/N]?"
read response

if [ "$response" == "Y" ] || [ "$response" == "y" ]; then
rsync -auvz --no-motd $EXTRA_OPT --exclude-from=${EXCLUDE_FILE} ${CWD}/ $CLUSTER:${REMOTE_PATH} 
else
echo "Canceling upload"
fi

# addJobToCalcs $CLUSTER 
echo
echo Remote path: $CLUSTER:$REMOTE_PATH

