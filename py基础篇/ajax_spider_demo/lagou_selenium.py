#encoding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from lxml import etree
import time
import re
import csv

class LagouSpider(object):
    # chromedriver的绝对路径
    driver_path = r'D:\ProgramApp\chromedriver\chromedriver.exe'
    def __init__(self):
        # 初始化一个driver，并且指定chromedriver的路径
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.positions = []
        self.fp = open('lagou.csv','a',encoding='utf-8',newline='')
        self.writer = csv.DictWriter(self.fp,['title','salary','city','work_years','education',"company_website",'desc','acquire','origin_url'])
        self.writer.writeheader()

    def run(self):
        url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.driver.get(url)
        while True:
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'pager_next')]"))
            )
            resource = self.driver.page_source
            self.parse_list_page(resource)
            next_btn = self.driver.find_element_by_xpath("//span[contains(@class,'pager_next')]")
            if "pager_next_disabled" in next_btn.get_attribute('class'):
                break
            next_btn.click()
            time.sleep(1)

    def parse_list_page(self,resource):
        html = etree.HTML(resource)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.parse_detail_page(link)
            time.sleep(1)

    def parse_detail_page(self,url):
        self.driver.execute_script("window.open('"+url+"')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located((By.XPATH,"//dd[@class='job_bt']"))
        )
        resource = self.driver.page_source
        html = etree.HTML(resource)
        title = html.xpath("//span[@class='name']/text()")[0]
        company = html.xpath("//h2[@class='fl']/text()")[0].strip()
        job_request_span = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_span[0].xpath(".//text()")[0]
        salary = salary.strip()
        city = job_request_span[1].xpath(".//text()")[0]
        city = re.sub(r"[/\s]","",city)
        work_years = job_request_span[2].xpath(".//text()")[0]
        work_years = re.sub(r"[/\s]","",work_years)
        education = job_request_span[3].xpath(".//text()")[0]
        education = re.sub(r"[/\s]","",education)
        company_website = html.xpath("//ul[@class='c_feature']/li[last()]/a/@href")[0]
        position_desc = "".join(html.xpath("//dd[@class='job_bt']/div//text()"))
        position = {
            'title': title,
            'city': city,
            'salary': salary,
            'company': company,
            'company_website': company_website,
            'education': education,
            'work_years': work_years,
            'desc': position_desc,
            'origin_url': url
        }
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.write_position(position)

    def write_position(self,position):
        if len(self.positions) >= 100:
            self.writer.writerows(self.positions)
            self.positions.clear()
        self.positions.append(position)
        print(position)

def main():
    spider = LagouSpider()
    spider.run()

if __name__ == '__main__':
    main()