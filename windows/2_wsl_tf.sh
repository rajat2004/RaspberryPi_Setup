echo "Creating new env for tf"
conda create -n tf_python3 python=3.5

source activate tf_python3
echo "Installing tensorflow"

export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp35-cp35m-linux_x86_64.whl

pip3 install --ignore-installed --upgrade $TF_BINARY_URL

echo "Building darkflow"
cd ~
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
pip install cython
python3 setup.py build_ext --inplace
pip install -e .

echo "Installing opencv"
conda install -c menpo opencv
