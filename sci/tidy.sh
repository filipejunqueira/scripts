#!/bin/bash

file="$1"
bibtex-tidy --curly --space=4 --sort=year,name --duplicates --merge --drop-all-caps --escape --tidy-comments --backup $1

echo "Your bib file $1 has been tidyup!"

