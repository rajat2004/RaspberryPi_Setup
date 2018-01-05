echo "Begin by reading username,password,hostname"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh $user@$hostname "$( cat << EOT
echo "Executing"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y tightvncserver

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

echo "Installed Vncserver"

sudo apt-get install -y netatalk
sudo apt-get install -y avahi-daemon
sudo update-rc.d avahi-daemon defaults

FILE= "/etc/avahi/services/afpd.service"

sudo /bin/cat <<EOM >$FILE
<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
   <name replace-wildcards="yes">%h</name>
   <service>
      <type>_afpovertcp._tcp</type>
      <port>548</port>
   </service>
</service-group>
EOM

sudo /etc/init.d/avahi-daemon restart

echo "File Sharing enabled"

FILE= "/etc/avahi/services/rfb.service"

sudo /bin/cat <<EOM >$FILE
<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
  <name replace-wildcards="yes">%h</name>
  <service>
    <type>_rfb._tcp</type>
    <port>5901</port>
  </service>
  </service-group>
EOM

sudo /etc/init.d/avahi-daemon restart

echo "Sharing Pi screen to mac enabled"
EOT
