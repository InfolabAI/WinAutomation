import time
import pyautogui as pa
import os
import subprocess
from functions_initialization import *
from deprecated_functions_pyautogui import *
from functions_selenium import Manage_selenium_IE

init = Initialization()
msi = Manage_selenium_IE(init)
msi.end_to_end()
exit(0)

"""
print_config_identifier() 는 꼭 모든 단계를 타고 들어갈 필요없음. 아래와 같이 확인하며 진행필요. 확인하지 않으면, 제대로 이름을 적어도 안 될 수 있음.
- ww.<아래단계명>.print_config_identifier()
"""

path1 = soup.select("frame")[1]["src"]

# html element 이름이 q인 것을 찾습니다. (검색창)
inputElement = driver.find_element_by_name("q")
time.sleep(2)

# 검색창에 'www.ngle.co.kr'을 입력합니다.
inputElement.send_keys("www.ngle.co.kr")
time.sleep(2)

# 검색 내용을 보냅니다.
inputElement.submit()
time.sleep(2)

# 검색된 리스트 중 링크 텍스트에 'THE BEST BUSINESS PLAN'이 포함된 것을 찾습니다.
continue_link = driver.find_element_by_partial_link_text("THE BEST BUSINESS PLAN")
time.sleep(2)

# 해당 링크를 클릭합니다.
continue_link.click()
time.sleep(5)


breakpoint()
# WebDriver를 종료합니다. (브라우저 닫기)
driver.quit()
