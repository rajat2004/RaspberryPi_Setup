# Optimised OpenCV 3.3 install for Raspberry Pi 3

Tested on Raspberry Pi 3 (B), running Raspberry Jessie

Credits: taken from _pyimagesearch_. Modified for use  case.

_____________

## Running the Scripts

All to be executed on a ssh shell.

Firstly,
```
sudo raspi-config   # And change the filesystem to entire SD Card
sudo reboot

```

Then,

`bash 1_part.sh`

Then,

`sudo nano /etc/dphys-swapfile`

and change CONF_SWAPSIZE to 1024 MB (enable all four cores).

Then,

`bash 2_part.sh`

Then,

`sudo nano /etc/dphys-swapfile`

and change CONF_SWAPSIZE back to 100 MB (enable all four cores).

Finally,
`bash 3_part.sh`

_____________

## Warnings

All of this is done in the global work environment. As such, since raspberries are used for targeted applications, in priciple, I haven't used any environment as would have been preferable otherwise.
