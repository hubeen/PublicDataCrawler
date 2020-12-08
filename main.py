import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import getpass
from bs4 import BeautifulSoup
import os, re
import math

def downloads(hrefs):
    for href in hrefs:
        driver.execute_script(href)
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
        download = bs.find("a", attrs={"class": "btn_type05 down"})
        driver.execute_script(download['onclick'])
        while(True):
            # driver.find_element_by_id("MyID")).value_of_css_property("display")
            if(driver.find_element_by_id("popup_wrap").value_of_css_property("display") == "none"):
                break

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
                 "profile.content_settings.pattern_pairs.*.multiple-automatic-downloads": 1,
                 "download.prompt_for_download": False,
                 "profile.default_content_setting_values.automatic_downloads" : 1
                 }
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="./driver/chromedriver", chrome_options=options)
time.sleep(2)

#init
driver.get('https://www.open.go.kr/othicInfo/infoList/orginlInfoList.do')

time.sleep(5)
html =driver.page_source 
bs = BeautifulSoup(html, 'html.parser')
next_btn = driver.find_element_by_class_name("next")
total = driver.find_element_by_id("totalPage").text.replace(",","")
driver.execute_script("document.querySelector(\"select[name='veiwNum'] option\").value=\"" + total + "\";searchCallFn();")

# 로드 해올 때까지 대기
while(True):
    print(driver.find_elements_by_id("imgLoading"))
    if(driver.find_elements_by_id("imgLoading") == []):
        break

div = bs.find("div", attrs={"class":"info_list"})
lis = div.find_all("li")
hrefs = []


for li in lis:
    hrefs.append(li.find("a")['href'])

print("load complate")

downloads(hrefs)


driver.close()
