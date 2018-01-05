#!/bin/bash

# SSH into Pi
# Change the hostname to keep your pi unique
# Since ssh pi@raspberrypi.local is far too common
# You might run into issues with multiple pi's
# Unless you remember their Ip Addresses

echo "Begining by updating and upgrading your OS"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "Linux Platform Detected"
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install sshpass

elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Mac OS Platform Detected"
  # Check if Homebrew is installed
  which -s brew
  if [[ $? != 0 ]] ; then
    echo "Installing Homebrew"
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  else
    echo "Homebrew Detected"
    echo "Updating Brew"
    brew update
  fi

  # Check if sshpass is Installed

  if brew ls --versions sshpass > /dev/null; then
    echo "The package is installed"
  else
    brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
  fi


else
  echo "This script supports only UNIX, LINUX"
  echo "Exiting script"
  exit 1
fi

################

echo "Enter Current Hostname for Raspberry Pi"
echo "Default is raspberrypi"
echo "To use default, press Enter key"

read hostname

hostname_dir=./credentials/.hostname.txt

if [[ -z "$hostname" ]]; then
  hostname='raspberrypi.local'
fi

echo hostname=$hostname > $hostname_dir

###############

echo "Enter Username for Raspberry Pi"
echo "Defaults are pi"
echo "To use default, press Enter key"

read user

user_dir=./credentials/.user.txt

if [[ $user=='' ]]; then
  user='pi'
fi

echo user=$user > $user_dir

####################

echo "Enter Password for Raspberry Pi"
echo "Defaults are raspberry"
echo "To use default, press Enter key"

read password

password_dir=./credentials/.password.txt

if [[ $password=='' ]]; then
  password='raspberry'
fi

echo password=$password > $password_dir

###################

echo "Enter New Hostname for Raspberry Pi"
echo "Default is raspberrypi"
echo "To use default, press Enter key"

read n_hostname

n_hostname_dir=./credentials/.hostname.txt

if [[ $n_hostname=='' ]]; then
  n_hostname='raspberrypi.local'
fi

echo hostname=$n_hostname > $n_hostname_dir

###################

sshpass -p $password ssh -o StrictHostKeyChecking=no $user@$hostname << EOF
sudo hostnamectl set-hostname $n_hostname
hostnamectl
EOF

echo "Changed hostname to, " $n_hostname
