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
EOF
