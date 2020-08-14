#!/bin/bash

doi="$1"
doi_file="authordoi-list.txt"
getpaper $doi
getbib $doi >> $BIB
article=$(getbib $doi | grep -oP '\@article\{\K[^,]+')
month=$(getbib $doi | grep -oP 'month = \{\K[^}]+')
echo "$article$month $1" >> $doi_file
echo "$article$month $1 added to $doi_file" 
