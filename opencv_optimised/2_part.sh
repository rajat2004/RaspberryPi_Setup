echo "Begin by reading username,password,hostname"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh -t $user@$hostname << EOF
echo "Restarting swap space"
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start

cd ~/opencv-3.3.0/build/

make -j4
echo "make file done"
sudo make install
sudo ldconfig

echo "Now decrease CONF_SWAPSIZE to 100 MB. In /etc/dphys-swapfile"
EOF
