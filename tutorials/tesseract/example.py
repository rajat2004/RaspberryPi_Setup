from pytesseract import image_to_string
from PIL import Image

# Load up an image
print image_to_string(Image.open('captcha.png'))
