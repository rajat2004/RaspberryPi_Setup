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
