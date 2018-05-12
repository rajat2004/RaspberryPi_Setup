echo "Begin by reading username,password,hostname"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh -t $user@$hostname << EOF

sudo apt-get -y update
echo "Installing pip2"
sudo apt-get -y install python-pip

echo "Starting to install Tensorflow, for python 2"

sudo apt-get -y install libblas-dev liblapack-dev python-dev \
 libatlas-base-dev gfortran python-setuptools
sudo pip install \
 http://ci.tensorflow.org/view/Nightly/job/nightly-pi-zero/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp27-none-any.whl

echo "Test tensorflow"

echo "Installling magic wormhole, useful for file sharing"

pip install magic-wormhole

echo "Installing opencv 3"

sudo apt-get -y install python2.7-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
pip install numpy
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig

echo "Installing scipy and pandas"

pip install scipy
pip install pandas

EOF
