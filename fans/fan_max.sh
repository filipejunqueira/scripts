#!/bin/bash

cd ~/software/dell_fan_control/
sudo ./dell-bios-fan-control 0
sudo i8kfan 2 2
echo "Done - Fans should be on overdose mode! ;-)"


