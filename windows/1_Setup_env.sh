echo "Will install all necessary dependencies for the workshop"

echo "Begin by upgrading shell and subsystem"

sudo apt-get update
sudo apt-get upgrade

echo "Installing gcc"

sudo apt-get install gcc make build-essential gfortran

echo "Installing Anaconda3"

wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh

conda update conda
conda update anaconda

cd /usr/local/bin
sudo ln -s ~/anaconda2/bin/* .
sudo ln -s ~/homer/.//bin/* .

cd ~

echo "Installing pip"

sudo apt-get -y install python-pip python-dev build-essential
sudo pip install --upgrade pip

echo "Installing magic wormhole"
sudo pip install magic-wormhole

echo "Installing git"
sudo apt-get -y install git

echo "Installing sshpass"
sudo apt-get -y install sshpass

echo "Script has completely finished"
