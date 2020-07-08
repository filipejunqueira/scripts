#!/bin/bash
options_rsync='-ahHAX --super'
pwd_final="/media/filipejunqueira/ExternalHd/"
pwd_origin=$HOME

while read p; do
echo "Backing up $p to $pwd_final"
f_path="${pwd_origin}${p}"
sudo rsync $options_rsync $f_path $pwd_final
done <home_ls_all.txt
echo 'DONE'

