#encoding: utf-8

import pytesseract
from urllib import request
from PIL import Image
import time


pytesseract.pytesseract.tesseract_cmd = r"D:\ProgramApp\TesseractOCR\tesseract.exe"


while True:
    captchaUrl = "https://passport.lagou.com/vcode/create?from=register&refresh=1513081451891"
    request.urlretrieve(captchaUrl,'captcha.png')
    image = Image.open('captcha.png')
    text = pytesseract.image_to_string(image,lang='eng')
    print(text)
    time.sleep(2)




