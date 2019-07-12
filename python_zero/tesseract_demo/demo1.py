#encoding: utf-8

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\ProgramApp\TesseractOCR\tesseract.exe"

image = Image.open('c.png')

text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)