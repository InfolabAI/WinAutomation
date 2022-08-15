import pyautogui as pa
import os
import subprocess
from functions_initialization import *
from functions_manage_interface import Manage_interface
from functions_password_pdf import Password_pdf


class Manage_pdf(Manage_interface):
    def __init__(self, password_list):
        super().__init__()
        self.pw = Password_pdf(password_list)

    def process_kill(self):
        os.system(command_kill_format + exe_name_dict["pdf"])

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

        # 띄어쓰기 문제 해결 및 경로 문제 해결
        subprocess.Popen(f'"{tmp_path}\\{fname}"', shell=True)
        if self.mp.wait_with_class_name(20, 0.5, "classFoxitPhantom"):
            pass
        else:
            Msgbox.error("Foxit pdf가 켜지지 않았습니다.")

        #self.time.sleep(5)


    def print(self, fname):
        self.time.sleep(1)
        pa.hotkey("ctrl", "p")
        self.time.sleep(2)
        pa.press("enter")
        self.wait_print()

