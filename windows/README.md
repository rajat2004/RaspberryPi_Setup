# Install Bash for Windows

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
