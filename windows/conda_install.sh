wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh

conda update conda
conda update anaconda

echo "Installing opencv"
conda install -c menpo opencv
