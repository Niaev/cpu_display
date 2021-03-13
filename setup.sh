#!/bin/bash

echo "[+] setup.sh\n"

current=$(pwd)
exe=$current/cpu_display.py

echo "[+] turning cpu_display.py into an executable"
chmod +x $exe


echo "[+] setting cpu_display.py to be executed on login"
touch ~/.bash_login
echo "[+] writing in $(ls -a ~/.bash_login)"
echo $exe >> ~/.bash_login 

echo "\n[+] setting up complete!\n"
