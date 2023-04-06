import pytesseract
import cv2
from pdf2image import convert_from_path
pages = convert_from_path('sample.pdf', 500)
for page in pages:
    page.save(f'sample_{page}.jpg', 'JPEG')
    
img = cv2.imread('sample.jpg',0)
data = pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789')
print(data)
# from pyresparser import ResumeParser
# import nltk
# nltk.download('stopwords')
# data = ResumeParser('dhruvv.jpgsa').get_extracted_data()
# print(data)