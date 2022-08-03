#!/bin/bash

echo "Updating APT"
echo "%%%%%%%%%%%%"
sudo apt update && sudo apt -y upgrade 
echo "Updating SNAP"
echo "%%%%%%%%%%%%"
sudo snap refresh
echo "Updating Flatpak"
echo "%%%%%%%%%%%%"
flatpak update

