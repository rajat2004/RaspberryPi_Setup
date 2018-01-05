# Setup Scripts for Raspberry Pi

_Models Supported: RPi 0,1,2,3 (A,B)_  
_Recommended: RPi 3B, 0 (and 0 W)_  
_Tested on: Rpi 3B_

____________

## Running Scripts

Make all scripts executable

```
chmod u+x *.sh
```

Run one-by-one

Note: Skip 2, if OS is not macOS (or OSX)

____________

## Install environment dependencies

 `bash dependencies.sh`

____________

## Script Description

1. Configure.sh: Sets up SSH capability and alters hostname
2. Setup for Mac: Allows for VNC, file share using SMP on macOS (10.10+)
3. TF_Open CV: Installs optimised tensorflow,non-optimised Opencv.


-------

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
or
`localhost:8898`
----

## Cloning SD cards

[link](https://medium.com/a-swift-misadventure/backing-up-your-raspberry-pi-sd-card-on-mac-the-simple-way-398a630f899c)

----

## Additonal Resources:

1. A complete HAAR cascade tutorial: https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
