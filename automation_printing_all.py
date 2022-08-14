import time
import pyautogui as pa
import os
import subprocess
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import timings

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from functions_pyautogui import *

tmp_env = os.environ["TEMP"]
tmp_path = tmp_env + "\\pyauto"
command_del_tmp = "del /q /s /f " + tmp_path + "\\*"
command_kill_groupware = "taskkill /f /im SaViewX.exe"
command_kill_hwx = "taskkill /f /im XSViewer.exe"
command_kill_alzip_auirender = "taskkill /f /im auirender.exe"
command_kill_alzip = "taskkill /f /im Alzip.exe"
timeU = Sleep(0.5)

os.system("mkdir " + tmp_path)
###### Chrome WebDriver를 이용해 Chrome을 실행합니다.
#####driver =  webdriver.Ie('C:\\Users\\AdmiN\\automation\\driver\\ie\\IEDriverServer.exe')
#####gh_path = "http://g0.gh.or.kr"
#####
###### www.google.com으로 이동합니다.
######driver.get("http://www.google.com/search?q=사과")
#####driver.get(gh_path + "/jsp/Main.jsp")
#####time.sleep(2)
#####
#####'''
#####Explorer 로그인, 문서함, 원하는 화면 띄우기를 기다리기
#####'''
#####breakpoint()
######html = driver.page_source
######soup = bs(html)
#####
#####
#####'''
#####HTML 상에는 게시글 관련 코드가 없고, frame 내부로 한단계씩 타고 들어가며 새로운 html 을 가져와야 함
#####아래는 IE 전용 코드이고, chrome 은 다른 코드를 사용해야 함
#####https://stackoverflow.com/questions/28761461/i-am-not-able-to-switch-to-iframe-using-internet-explorer
#####'''
#####from selenium.webdriver.common.by import By
#####
#####driver.switch_to.frame(driver.find_element(By.NAME, 'Start'))
#####driver.switch_to.frame(driver.find_element(By.NAME, 'doc_frame_right'))
#####
#####'''
#####IE 의 개발자모드에서 HTML source 를 보며 게시글에 해당하는 element 를 가져옴
#####https://selenium-python.readthedocs.io/locating-elements.html
#####'''
#####elements = driver.find_elements(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[@class='Bsc']")
#####
###### 위 코드는 완벽하진 않지만, 예외적인 Bsc 를 모두 클릭해도 문제는 없음.
#####for html_el in elements:
#####    if html_el.size['width'] > 250:
#####        #size로 구분
#####        process_el = retry_click_until_process_open(html_el)
#####        breakpoint()
#####        print('d')


def saving_files_in_one_paper(name):
    """
    하나의 게시글의 모든 파일을 저장하는 함수
    """
    process_el = find_element_with_name(name)
    window = open_window_with_handle(process_el.handle)
    save_files_with_window(window)
    os.system(command_del_tmp)

    wait_for_process_open_with_name("다른 이름으로")
    pa.hotkey("ctrl", "l")
    pa.typewrite(tmp_path)
    pa.press("enter")
    pa.hotkey("alt", "s")

    timeU.sleep(2)
    os.system(command_kill_groupware)
    timeU.sleep(1)


def print_contents_in_files():
    file_list = os.listdir(tmp_path)
    for fname in file_list:
        if ".zip" in fname:
            os.system(command_kill_alzip)
            os.system(command_kill_alzip_auirender)
            # 띄어쓰기 문제 해결 및 경로 문제 해결
            subprocess.Popen(f'"{tmp_path}\\{fname}"', shell=True)
            process_el = wait_for_process_open_with_name(fname[:10])
            window = open_window_with_handle(process_el.handle)
            window.압축풀기Button.click()
            process_el_sub = wait_for_process_open_with_name("압축풀기")
            window_sub = open_window_with_handle(process_el_sub.handle)
            pa.typewrite(tmp_path)
            # 선택된 폴더 하위에 압축파일명으로 폴더 생성(F) 의 상태 확인 후 켜기
            while window_sub["선택된 폴더 하위에 압축파일명으로 폴더 생성"].get_toggle_state() == 0:
                window_sub["선택된 폴더 하위에 압축파일명으로 폴더 생성"].click()
                timeU.sleep(0.1)
            while window_sub["압축풀기 후 폴더열기"].get_toggle_state() == 1:
                window_sub["압축풀기 후 폴더열기"].click()
                timeU.sleep(0.1)
            pa.press("enter")

            timeU.sleep(0.1)
            process_password("비밀번호", ["1000", "1010", "1011", "1021"])
            # 알집 window 중복 문제 해결해야 함
            os.system(command_kill_alzip)
            os.system(command_kill_alzip_auirender)

        if ".hwx" in fname:
            # 띄어쓰기 문제 해결 및 경로 문제 해결
            subprocess.Popen(f'"{tmp_path}\\{fname}"', shell=True)
            wait_for_process_open_with_name(fname[:10])
            pa.hotkey("ctrl", "p")
            pa.hotkey("alt", "d")
            wait_for_process_open_with_name("인쇄")
            wait_for_process_kill_with_name("인쇄")
            os.system(command_kill_hwx)


print_contents_in_files()
breakpoint()


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
