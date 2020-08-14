#!/bin/bash

cat "$1" | xclip
$BROWSER --app=https://flamingtempura.github.io/bibtex-tidy/
echo $("$1 has been copied to the clipboard")
