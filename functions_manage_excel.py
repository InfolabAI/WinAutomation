import pyautogui as pa
import os
import subprocess
import pywinauto
from pywinauto.timings import wait_until
from functions_process import Manage_process
from functions_initialization import *
from functions_manage_interface import Manage_interface
from functions_password_excel import Password_excel


class Manage_excel(Manage_interface):
    def __init__(self, password_list):
        super().__init__()
        self.mp = Manage_process()
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
        self.time.sleep(1)

        # 띄어쓰기 문제 해결 및 경로 문제 해결
        subprocess.Popen(f'"{tmp_path}\\{fname}"', shell=True)
        self.mp.wait_with_class_name(10, 0.1, "XLMAIN")

        # 지난번 실행 시, 오류가 있었다는 창 없애기
        # window = self.mp.open_window_with_handle(
        #    self.mp.wait_for_process_open_with_name("Microsoft Excel").handle
        # )
        # if "마지막" in window.Static1.window_text():
        if self.mp.wait_with_class_name(10, 0.1, "#32770"):
            # window.Button1.click()
            self.time.sleep(1)
            pa.hotkey("alt", "y")

    def print(self, fname):
        self.time.sleep(1)
        pa.hotkey("ctrl", "p")
        self.time.sleep(5)
        # pa.press("enter")
        ## pa.hotkey("alt", "d")
        # self.mp.wait_for_process_open_with_name("인쇄")
        # self.mp.wait_for_process_kill_with_name("인쇄")
        self.time.sleep(1)

