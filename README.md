# **cpu_display**

<p align="center">
    <img src="logo.png">
</p>

`cpu_display` is a python script for displaying CPU usage and temperature in a LCD (16x2) using I2C module, for Raspberry Pi.

## **Requirements**

### Hardware

* Any Raspberry Pi model (I think so, at least, [let me know](https://github.com/Niaev/cpu_display/issues) if you have any trouble with your model);
* Liquid Crystal Display 16x2;
* I2C Module;
* Some cables

### Software

For `cpu_display` to work in your Raspberry Pi, not depending on the operating system you are using, you may need to install some packages:

* `lm-sensors`
* `python3-smbus`
* `python3-rpi.gpio`
* `i2c-tools`

And enable I2C interface through `raspi-config`, following those steps:

* Type `sudo raspi-config` in your terminal
* Select **"Interface Options"**
* Select **"P5 I2C"**
* Select **"Yes"**, to enable I2C interface

## **Installation**

If you want `cpu_display` to work at startup or login, you will need to run `setup.sh` script. If you don't want to, you can just execute the main script alone:

```
./cpu_display.py
```

Requirements satisfied, you can now setup `cpu_display`, typing the following line in your terminal:

```
sudo sh setup.sh
```

`setup.sh` may need to edit `/etc/rc.local`, a file that requires superuser access, so don't forget the `sudo` command at the beginning.

## **Usage and how it works**

The output of the script will be the following, if everything is correct with the requirements previously described.

```
[+] LCD detected!
[+] Writing information...
```

If you can see this output after running the script, your LCD is probably displaying stuff.

The info displayed is changed every 2 seconds. CPU temperature displayed is retrieved from the `sensors` command and usage is from `/proc/stat`, both are stored in a temporary file and then formatted into your LCD.