#!/bin/bash

echo "input the year and session (in this order) and I'll download everything"
read year session

echo "Downloading..."
scp -r pil64133@ssh.diamond.ac.uk:/dls/i09/data/$year/$session/ .

