import pyautogui as pa
import os
import subprocess
from functions_initialization import *
from functions_manage_interface import Manage_interface
from functions_password_hwp import Password_hwp


class Manage_hwp(Manage_interface):
    def __init__(self, password_list):
        super().__init__()
        self.pw = Password_hwp(password_list)

    def process_kill(self):
        os.system(command_kill_format + exe_name_dict["hwp"])

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
        #self.time.sleep(1)

        self.is_process_open(fname, "HwpApp : 9.0")

        self.time.sleep(5)

    def print(self, fname):
        self.time.sleep(1)
        pa.hotkey("ctrl", "p")
        self.time.sleep(2)
        pa.press("enter")
        self.wait_print()