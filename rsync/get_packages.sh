#!/bin/bash

dpkg --get-selections > installed-packages
apt-key exportall > repo-keys

