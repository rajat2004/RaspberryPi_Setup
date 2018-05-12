# Setup Scripts for Raspberry Pi

These are a bunch of install, utility and tutorial scripts we commonly use for the raspberry pi.

_Author: Varun Sundar_

_Last Updated: 11th April, 2018_

_Models Supported: RPi 0,1,2,3 (A,B)_  
_Recommended: RPi 3B, 0 (and 0 W)_  
_Tested on: Rpi 3B_

## RoadMap

[X] Unify all three major platforms
[ ] Update tensorflow to 1.8.1
[ ] Shift to Python 3 on the pi. (Currently, python2 is the defacto standard)

## Running the Scripts

* Make all scripts executable

```
chmod u+x *.sh
```

* Run one-by-one, from the parent folder.

 As `bash utils/xyz.sh`

* Note: Skip 2_Setup_for_Mac.sh, if OS is not macOS (or OSX)

## Folder Descriptions

### Utils

1. Configure.sh: Sets up SSH capability and alters hostname
2. Setup for Mac: Allows for VNC, file share using SMP on macOS (10.10+)
3. TF_Open CV: Installs optimised tensorflow,non-optimised Opencv.
  * This is available for both Raspberry pi zero and 3B.
4. Install Darkflow
5. Installs OpenCV 3 (non-optimised)
6. Install pytersseract.

## Optimised OpenCV 3.3 install for Raspberry Pi 3

Tested on Raspberry Pi 3 (B), running Raspberry Jessie

Credits: taken from _pyimagesearch_. Modified for usecase.

### Running the Scripts

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

### Warnings

All of this is done in the global work environment. As such, since raspberries are used for targeted applications, in priciple, I haven't used any environment as would have been preferable otherwise.

## Windows

Compatible with WSL (Windows Subsytem for Linux)

Follow either this: https://docs.microsoft.com/en-us/windows/wsl/install-win10

Or this: https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10

Once your shell (bash) is up and running, execute the following:

```
cd ~
sudo apt-get install wget
wget  https://raw.githubusercontent.com/varun19299/Raspberry-Pi-Setup/master/windows/1_Setup_env.sh
bash 1_Setup_env.sh
```

You can choose to retain the blank password or change it:

```
sudo passwd    # Change root password
```

You can then use the remaining scripts in `windows` to install tensorflow and pytersseract.

## Tutorials

Contains a bunch of tutorials that have been run and optimised for the Raspberry pi.

Includes common Computer Vision algorithms (cascades), a couple of CNNs and SSD nets.

# Miscellaneous

## Running remote jupyter notebooks:

Step 1: ssh into the remote-machine
`ssh user@host`

Step 2: [optional] On the remote-machine, run tmux
`tmux`
If your remote session gets disconnected, tmux will keep the session running (to reconnected run tmux attach)!

Step 3: On the remote-machine, navigate to the folder containing your Jupyter Notebook:
`cd //path/to/my/code`

Step 4: On the remote-machine, run the notebook with these flags
`jupyter notebook --no-browser --port=8898`
where the --no-browser means don’t open the internet browser, and --port=8898 means to run it using this port. You can change the port number to something else as well.

This should start an IPython/Jupyter Notebook and you should see something like:
```
...
[I 10:54:08.168 NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8898/
[I 10:54:08.168 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Step 5: On your local-machine, use ssh with port forwarding
`ssh -N -f -L 127.0.0.1:8898:127.0.0.1:8898 jer@remote-machine`
This sets the port 8898 on your local-machine to forward to port 8898 on your remote-machine. Make sure that this port number matches the port number in Step 4. You can also change the port numbers both on your remote and local machine as needed (and they do not have to match)

Step 6: On your local-machine, open your internet browser and type in,
`http://127.0.0.1:8898`
`localhost:8898`

## Cloning SD cards

[link](https://medium.com/a-swift-misadventure/backing-up-your-raspberry-pi-sd-card-on-mac-the-simple-way-398a630f899c)

## Windows dhcpserver

Makes connecting to a pi on windows far easier.

1. Download DHCP Server for Windows. It is a 100kB download available here. http://www.dhcpserver.de/cms/
2. Go to the IPv4 properties page of the Ethernet adapter and set a fixed IP address, say 192.168.2.1
3. Run the DHCP Server Wizard (downloaded above)
4. Select the Ethernet adapter from the list shown
5. Save the configuration file and start up the DHCP Server
6. Click the 'Continue as tray app' button in the server control panel.
7. Boot up the Raspberry Pi
8. A popup notification shows the IP address assigned by the DHCP server to the Raspberry Pi.
9. Use a SSH client, like PuTTy, to connect to the IP address shown


## Additonal Resources:

1. A complete HAAR cascade tutorial: https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
