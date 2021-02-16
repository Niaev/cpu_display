#!/usr/bin/env python3

# imports
import drivers
from time import sleep
import os, sys

try:
    try:
        # init display
        display = drivers.Lcd()
    except OSError as e:
        print("[+] No LCD connected!")
        print("[+] Shutting down...")
        sys.exit()

    print("[+] LCD detected!")
    print("[+] Writing information...")
    display.lcd_backlight(1) # turn on backlight

    # loop
    while True:
        # get cpu temperature and usage from os info
        os.system("sensors | grep temp1: > .tmp/temp.txt") 
        os.system("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}' >> .tmp/temp.txt")

        # read temporary file with values
        with open('.tmp/temp.txt','r') as f:
            text = f.read().split('\n')
            temp = text[0].split('+')[1] # get temperature
            usag = text[1] # get usage
    
        # formatting values
        temp = temp.replace('°','o')
        usag = '{:.2f}'.format(float(usag))

        # display values
        display.lcd_display_string(f'Temp.: {temp}',1)
        display.lcd_display_string(f'Usage: {usag}%',2)
    
        sleep(2) # wait
except KeyboardInterrupt as e:
    print("\n[+] Shutting down...")
    display.lcd_clear()
    sys.exit()
