echo "Begin by reading username,password,hostname"

hostname_dir=./credentials/.hostname.txt
user_dir=./credentials/.user.txt
password_dir=./credentials/.password.txt

source $hostname_dir; echo "Reading hostname"
source $user_dir; echo "Reading user (name)"
source $password_dir; echo "Reading password"

echo $hostname

sshpass -p $password ssh -t $user@$hostname << EOF
cd ~
wget http://www.leptonica.org/source/leptonica-1.73.tar.gz
tar -zxvf leptonica-1.73.tar.gz
cd leptonica-1.73
./configure
make
sudo checkinstall
sudo ldconfig

cd ~
git clone https://github.com/tesseract-ocr/tesseract.git
cd tesseract
./autogen.sh
./configure
make
sudo make install
sudo ldconfig

cd ~
git clone https://github.com/tesseract-ocr/tessdata.git
sudo mv ~/tessdata/* /usr/local/share/tessdata/

echo "Test tesseract now"
echo "Try: tesseract img.png out"
echo "Output will be saved under out.txt"

sudo pip install pytesseract
pip install pillow
EOF
