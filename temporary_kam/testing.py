import pytesseract
from PIL import Image
import os
import cv2
from PIL import Image
  
# Open the image by specifying the image path.
image_path = "pics/page2.png"
image_file = Image.open(image_path)
  
# the default
image_file.save("image_name.jpg", quality=95)

# tatte = []
# for i in os.listdir('pics'):
#     # print(i)
#     tatte.append(pytesseract.image_to_string(Image.open('pics/' + i)))

print(pytesseract.image_to_string('image_name.jpg'))

