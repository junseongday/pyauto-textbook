# from selenium import webdriver
# import os, time, datetime
# from _MyPath import URL, DRIVER as d

# # 접속할 URL 지정 --- (1)
# url = URL+'book'

# # 저장 경로 및 파일 이름 --- (2)
# save_dir = os.path.abspath('./output')
# save_file = os.path.join(save_dir, 'download_booklist.csv')

# # 크롬 옵션에 저장 경로 설정 --- (3)
# options = webdriver.ChromeOptions()
# options.add_experimental_option('prefs', {
#     'download.default_directory': save_dir})

# # 메인 처리 --- (4)
# def csv_download():
#     # 기존 파일 삭제 --- (5)
#     delete_file()
#     # 'CSV 다운로드' 버튼 클릭 --- (6)
#     driver = webdriver.Chrome(d, options=options)
#     driver.get(url)    
#     btn  = driver.find_element_by_partial_link_text('CSV') #--- (6a)
#     btn.click() #--- (6b)
#     # 파일 다운로드 확인 --- (7)
#     if check_file():
#         print("다운로드 완료")
#         print_file()
#     else:
#         print("다운로드 실패")
#     driver.quit()

# # 파일 존재 여부 확인 --- (8)
# def check_file():
#     for i in range(30):
#         if os.path.exists(save_file): #--- (8a)
#             return True
#         time.sleep(1)
#     return False

# # 파일 내용 출력        
# def print_file():
#     with open(save_file, 'r', encoding='utf-8') as f:
#        text = f.read()
#        print(text)
       
# # 기존 파일 삭제
# def delete_file():
#     if os.path.exists(save_file):
#         os.remove(save_file)
#         print('기존 파일 삭제')

# if __name__ == '__main__':
#         csv_download()  

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os, time, datetime
from _MyPath import URL, DRIVER as d
from selenium.webdriver.common.by import By

# 접속할 URL 지정 --- (1)
url = URL+'book'

# 저장 경로 및 파일 이름 --- (2)
save_dir = os.path.abspath('./output')
save_file = os.path.join(save_dir, 'download_booklist.csv')

# 크롬 옵션에 저장 경로 설정 --- (3)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('prefs', {
    'download.default_directory': save_dir})

# 메인 처리 --- (4)
def csv_download():
    # 기존 파일 삭제 --- (5)
    delete_file()
    # 'CSV 다운로드' 버튼 클릭 --- (6)
    service = ChromeService(executable_path=d)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    driver.find_element
    btn  = driver.find_element(By.PARTIAL_LINK_TEXT, 'CSV') #--- (6a)
    btn.click() #--- (6b)
    # 파일 다운로드 확인 --- (7)
    if check_file():
        print("다운로드 완료")
        print_file()
    else:
        print("다운로드 실패")
    driver.quit()

# 파일 존재 여부 확인 --- (8)
def check_file():
    for i in range(30):
        if os.path.exists(save_file): #--- (8a)
            return True
        time.sleep(1)
    return False

# 파일 내용 출력        
def print_file():
    with open(save_file, 'r', encoding='utf-8') as f:
       text = f.read()
       print(text)
       
# 기존 파일 삭제
def delete_file():
    if os.path.exists(save_file):
        os.remove(save_file)
        print('기존 파일 삭제')

if __name__ == '__main__':
        csv_download()  
