import pyautogui as pa
import os
import subprocess
from functions_initialization import *
from functions_manage_interface import Manage_interface
from functions_password_excel import Password_excel


class Manage_excel(Manage_interface):
    def __init__(self, password_list):
        super().__init__()
        self.pw = Password_excel(password_list)

    def process_kill(self):
        os.system(command_kill_format + exe_name_dict["excel"])

    def run(self, fname):
        """
        전체 실행을 담당한다"""
        self.process_kill()
        self.process(fname)
        self.password_cycle(fname)
        self.print(fname)
        self.process_kill()

    def process(self, fname):
        """
        file을 print 함
        
        Args:
            fname: print할 파일의 이름
            file_type: print할 파일의 type (exe_name_dict 확인)"""
        # 너무 빨리 다시 실행하면 프로세스가 완전히 종료되기 전이기 때문에 1초 기다림
        #self.time.sleep(5)

        # 띄어쓰기 문제 해결 및 경로 문제 해결
        subprocess.Popen(f'"{tmp_path}\\{fname}"', shell=True)
        # 켜졌는지 확인
        if self.mp.wait_with_class_name(20, 0.5, "XLMAIN"):
            pass
        else:
            Msgbox.error("Excel이 켜지지 않았습니다.")

        self.time.sleep(5)
        # 지난번 실행 시, 오류가 있었다는 창 없애기
        # window = self.mp.open_window_with_handle(
        #    self.mp.wait_for_process_open_with_name("Microsoft Excel").handle
        # )
        # if "마지막" in window.Static1.window_text():
        #if self.mp.wait_with_class_name(10, 0.1, "#32770"):
        #    # window.Button1.click()
        #    self.time.sleep(1)
        #    pa.hotkey("alt", "y")

    def print(self, fname):
        self.time.sleep(1)
        pa.hotkey("ctrl", "p")
        self.time.sleep(2)

        window = self.mp.open_window_with_class_name("XLMAIN", uia=True)
        if '현재 설정된 용지' in window['크기조정ComboBox'].wrapper_object().selected_text():
            window['크기조정ComboBox'].wrapper_object().expand()
            self.time.sleep(1)
            pa.press('down', 2)
            pa.press('enter')
        if '한 페이지에 시트' in window['크기조정ComboBox'].wrapper_object().selected_text():
            window['크기조정ComboBox'].wrapper_object().expand()
            self.time.sleep(1)
            pa.press('down', 1)
            pa.press('enter')
        if '한 페이지에 모든 행' in window['크기조정ComboBox'].wrapper_object().selected_text():
            window['크기조정ComboBox'].wrapper_object().expand()
            self.time.sleep(1)
            pa.press('up', 1)
            pa.press('enter')

        self.time.sleep(1)
        pa.press("enter")
        self.wait_print()

