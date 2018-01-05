echo "Begin by reading username,password,hostname"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh -t $user@$hostname << EOF
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
pip install cython
python3 setup.py build_ext --inplace
pip install -e .

echo "Installing Jupyter"
python -m pip install --upgrade pip
python -m pip install jupyter

echo "Starting jupyter"
jupyter notebook --no-browser --port=8898
EOF

ssh -N -f -L 127.0.0.1:8898:127.0.0.1:8898 $user@$hostname

echo "Open http://127.0.0.1:8898 or localhost:8898"
