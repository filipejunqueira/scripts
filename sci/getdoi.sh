#!/bin/bash
[ -z "$1" ] && echo "Give either a pdf file or a url as an argument." && exit

if [ -f "$1" ]; then
	# Try to get DOI from pdfinfo or pdftotext output.
	doi=$(pdfinfo "$1" | grep -io "doi:.*") ||
	doi=$(pdftotext "$1" 2>/dev/null - | grep -io "doi:.*" -m 1) ||
	echo "$doi" ||
	exit 1 
else
	url="$1"


        # Check crossref.org for the bib citation.
        ref=$(curl -s "http://api.crossref.org/works/$url/transform/application/x-bibtex" -w "\\n")

	doi=$(echo $ref | grep -oP 'doi = \{\K[^}]+')
        echo $doi	

fi
