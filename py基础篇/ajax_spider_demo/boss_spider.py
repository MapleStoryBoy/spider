#encoding: utf-8

from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
import pytesseract
from urllib import request
from PIL import Image
import re

class BossSpider(object):
    driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=BossSpider.driver_path)
        pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramApp\TesseractOCR\tesseract.exe'
        self.url = 'https://www.zhipin.com/c100010000/h_101250100/?query=python'
        self.domain = "https://www.zhipin.com"
        fp = open('boss.csv','a',newline='',encoding='utf-8')
        self.writer = csv.DictWriter(fp,['name','company_name','salary','city','work_years','education','desc'])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        while True:
            if len(self.driver.find_elements_by_id("captcha")) > 0:
                self.fill_captcha()
                time.sleep(2)
                continue
            source = self.driver.page_source
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//a[contains(@class,'next')]")
            if "disabled" in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()

    def fill_captcha(self):
        captchaInput = self.driver.find_element_by_id("captcha")
        captchaImg = self.driver.find_element_by_class_name("code")
        submitBtn = self.driver.find_element_by_class_name('btn')
        src = captchaImg.get_attribute('src')
        request.urlretrieve(self.domain + src, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        captcha = re.sub(r"[\s/]","",text)
        captchaInput.send_keys(captcha)
        submitBtn.click()


    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//div[@class='info-primary']//a[position()=1]/@href")
        for link in links:
            url = self.domain+link
            self.request_detail_page(url)
            time.sleep(1)

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        name = html.xpath("//div[@class='name']/text()")[0].strip()
        salary = html.xpath("//div[@class='name']/span[@class='badge']/text()")[0].strip()
        infos = html.xpath("//div[@class='job-primary']/div[@class='info-primary']/p//text()")
        city = infos[0]
        work_years = infos[1]
        education = infos[2]

        company_name = html.xpath("//a[@ka='job-detail-company']/text()")[0]
        desc = html.xpath("//div[@class='job-sec']/div[@class='text']//text()")
        desc = "\n".join(desc).strip()
        position = {
            'name': name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc
        }
        self.write_position(position)

    def write_position(self,position):
        self.writer.writerow(position)
        print(position)

if __name__ == '__main__':
    spider = BossSpider()
    spider.run()