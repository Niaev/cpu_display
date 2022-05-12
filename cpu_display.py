#!/usr/bin/env python3
"""Displays CPU info to a Liquid Crystal Display"""

import os
import sys
from time import sleep

import drivers

try:
    # Setup section
    try:
        # Init display
        display = drivers.Lcd()
    except OSError as e:
        print("[+] No LCD connected!")
        print("[+] Shutting down...")
        sys.exit()

    print("[+] LCD detected!")
    print("[+] Writing information...")
    display.lcd_backlight(1) # Turn on backlight

    # Loop section
    while True:
        # Get cpu temperature and usage from os info
        os.system("sensors | grep temp1: > /tmp/temp.txt") 
        os.system("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}' >> /tmp/temp.txt")

        # Read temporary file with values
        with open('/tmp/temp.txt','r') as f:
            text = f.read().split('\n')
            temp = text[0].split('+')[1] # Get temperature
            usag = text[1] # Get usage
    
        # Formatting values
        temp = temp.replace('°','o')
        usag = '{:.2f}'.format(float(usag))

        # Adding spaces to the end to fit in 16 char line
        temp = '%-16s' % temp
        usag = '%-16s' % (usag + '%')

        # Display values
        display.lcd_display_string(f'Temp.: {temp}',1)
        display.lcd_display_string(f'Usage: {usag}',2)
    
        sleep(2) # Wait
except KeyboardInterrupt as e:
    print("\n[+] Shutting down...")
    display.lcd_clear()
    sys.exit()
