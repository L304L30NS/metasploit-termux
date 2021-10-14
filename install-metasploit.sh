#!bin/bash
cd $HOME
pkg install python wget -y
python -m pip install --upgrade pip
pip install colorama
### link ###
wget https://raw.githubusercontent.com/Learn-Termux/metasploit-termux/main/msf.py
###        ###
clear
python msf.py
