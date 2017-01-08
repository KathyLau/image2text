from pytesser import *
from PIL import Image
#import subprocess
#import util
#import errors

image = Image.open('fonts_test.png')
# Open image object using PIL
print image_file_to_string(image)
# Run tesseract.exe on image fnord
#print image_file_to_string('fnord.tif')# fnord ```
