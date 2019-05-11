#!/bin/sh

echo 'Installing Required Software'
yes | sudo apt-get install ffmpeg
yes | sudo apt-get install sshpass

echo 'Installing Python Libraries'
yes | pip install matplotlib.pyplot
yes | pip install subprocess
yes | pip install paramiko

# EOF