echo "Preparing environment"
echo "Environment name is rpiforiot"

conda create -y -n rpiforiot python=3.5

source activate rpiforiot

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "Linux Platform Detected"

  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp35-cp35m-linux_x86_64.whl

elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Mac OS Platform Detected"

  export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow_gpu-0.12.1-py3-none-any.whl

  fi

echo "Installing tensorflow CPU"

pip install --ignore-installed --upgrade $TF_BINARY_URL

echo "Installing opencv3"

conda install -y -c menpo opencv3
