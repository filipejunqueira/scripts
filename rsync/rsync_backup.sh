#!/bin/bash
options_rsync='-avhH --super --progress --delete'
pwd_final="/media/captainbroccoli/HOME_DESKTOP"
pwd_origin="/home/captainbroccoli/"

while read p; do
echo "Backing up $p to $pwd_final"
f_path="${pwd_origin}${p}"
sudo rsync $options_rsync $f_path $pwd_final
done <home_ls_all.txt
echo 'DONE'

