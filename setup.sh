#!/bin/bash

echo "[+] setup.sh\n"

current=$(pwd)
exe=$current/cpu_display.py

echo "[+] turning cpu_display.py into an executable"
chmod +x $exe

pcname=$(uname -a | cut -d " " -f 2)

if [ $pcname = "retropie" ] ; then 
    sed -i 's/exit 0//g' /etc/rc.local
    echo "cd $current" >> /etc/rc.local
    echo "python3 cpu_display.py &" >> /etc/rc.local
    echo "cd /" >> /etc/rc.local
    echo "exit 0" >> /etc/rc.local
    echo "[+] rc.local edited! cpu_display.py setted to be executed on startup"
else
    echo "[+] setting cpu_display.py to be executed on login"
    touch ~/.bash_login
    echo "[+] writing in $(ls -a ~/.bash_login)"
    echo $exe >> ~/.bash_login 
fi

echo "\n[+] setting up complete!\n"
