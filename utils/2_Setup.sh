echo "Will install vncserver"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh -t $user@$hostname << EOF
echo "Executing"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install tightvncserver

cd /home/pi
cd .config
mkdir autostart
cd autostart

FILE= "tightvnc.desktop"

/bin/cat <<EOM >$FILE
[Desktop Entry]
Type=Application
Name=TightVNC
Exec=vncserver :1
StartupNotify=false
EOM

echo "Installed Vncserver, Running now"
vncserver :1

EOF
