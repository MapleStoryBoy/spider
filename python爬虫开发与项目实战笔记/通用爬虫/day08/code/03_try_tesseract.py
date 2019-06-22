# coding=utf-8
from PIL import Image
import pytesseract

file_path = "/Users/zdw/Documents/work/备课/爬虫/图片/tesseracttest1.jpg"
file_path = "/Users/zdw/Documents/work/备课/爬虫/图片/tess2.jpg"
img = Image.open(file_path)
print(pytesseract.image_to_string(img))