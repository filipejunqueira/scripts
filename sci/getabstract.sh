#!/bin/bash

doi="$1"
metadata=$(curl -LH "Accept:application/vnd.crossref.unixref+xml" http://dx.crossref.org/$doi)

echo $metadata

abstract=$(echo $metadata | grep "abstract")
echo $abstract


