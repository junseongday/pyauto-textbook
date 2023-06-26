# from selenium import webdriver
# import time
# from _MyPath import URL, DRIVER as d

# # 책 소개 사이트 열기 --- (1)
# driver = webdriver.Chrome(d)
# driver.get(URL)

# # title 및 div.title 요소 가져오기 --- (2)
# title = driver.find_element_by_tag_name('title')
# div = driver.find_element_by_class_name('title')

# # text 속성 출력 --- (3)
# print('---------text---------')
# print('<title>:', title.text) #빈 문자열
# print('<div>:', div.text) #빈 문자열

# #display 여부 출력 --- (4)
# print('---------is_displayed()---------')
# print('<title>:', title.is_displayed())
# print('<div>:',div.is_displayed())

# # innerText 속성 가져오기 --- (5)
# print('---------innerText---------')
# print('<title>:', title.get_attribute('innerText'))
# print('<div>:',div.get_attribute('innerText'))

# time.sleep(3)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from _MyPath import URL, DRIVER as d
from selenium.webdriver.common.by import By

# 책 소개 사이트 열기 --- (1)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = ChromeService(executable_path=d)
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

# title 및 div.title 요소 가져오기 --- (2)
title = driver.find_element(By.CSS_SELECTOR, 'title')
div = driver.find_element(By.CSS_SELECTOR, '.title')

# text 속성 출력 --- (3)
print('---------text---------')
print('<title>:', title.text) #빈 문자열
print('<div>:', div.text) #빈 문자열

#display 여부 출력 --- (4)
print('---------is_displayed()---------')
print('<title>:', title.is_displayed())
print('<div>:',div.is_displayed())

# innerText 속성 가져오기 --- (5)
print('---------innerText---------')
print('<title>:', title.get_attribute('innerText'))
print('<div>:',div.get_attribute('innerText'))

time.sleep(3)
driver.quit()
