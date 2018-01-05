echo "Begin by reading username,password,hostname"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh -t $user@$hostname << EOF

echo "Starting to install Tensorflow, for python 2"

sudo apt-get -y install libblas-dev liblapack-dev python-dev \
 libatlas-base-dev gfortran python-setuptools
​pip install \
 http://ci.tensorflow.org/view/Nightly/job/nightly-pi/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp27-none-any.whl

echo "Test tensorflow"

echo "Installling magic wormhole, useful for file sharing"

pip install magic-wormhole

echo "Installing numpy,scipy and pandas"

pip install numpy
pip install scipy
pip install pandas

echo "Installing flask"
pip install flask
EOF
