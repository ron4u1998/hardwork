import pytesseract
import cv2
from pdf2image import convert_from_path
from paddleocr import PaddleOCR

# pages = convert_from_path('sample.pdf', 500)
# for page in pages:
#     page.save(f'sample_{page}.jpg', 'JPEG')
    
img = cv2.imread('sample4.jpg',0)
# data = pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789')
# print(data)

Paddle = PaddleOCR(lang='en',  det_db_score_mode='slow', use_dilation=True,  show_log=False)
output = Paddle.ocr(img)
texts = [line[1][0] for line in output]
print(texts)
# from pyresparser import ResumeParser
# import nltk
# nltk.download('stopwords')
# data = ResumeParser('dhruvv.jpgsa').get_extracted_data()
# print(data)