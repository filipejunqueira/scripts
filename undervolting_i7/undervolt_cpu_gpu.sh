#!/bin/bash

cd ~/software/intel_undervolt/linux-intel-undervolt-tool/
sudo undervolt -cpu -100 -gpu -100
sudo echo "Done - FANS on MAX, CPU -100mV and GPU -100mv"
