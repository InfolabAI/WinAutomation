import time
import pyautogui as pa
import os
import subprocess
from functions_initialization import *
from deprecated_functions_pyautogui import *
from functions_print_files_in_a_folder import Print_files_in_a_folder

Initialization()
password_input = "1010, 1011"
pff = Print_files_in_a_folder(password_list=password_input.split(","))
pff.print_files_in_a_folder(tmp_path)
exit(0)


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
            os.system(command_kill_format + exe_name_dict["hwx"])


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
