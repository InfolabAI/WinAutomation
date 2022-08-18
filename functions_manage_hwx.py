import pyautogui as pa
import os
import subprocess
from functions_initialization import *
from functions_manage_interface import Manage_interface


class Manage_hwx(Manage_interface):
    def __init__(self, password_list):
        super().__init__()

    def process_kill(self):
        os.system(command_kill_format + exe_name_dict["hwx"])

    def run(self, fname):
        """
        전체 실행을 담당한다"""
        self.process_kill()
        self.process(fname)
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
        '''
        에러
            파일명: 01-1.매입임대주택 공급관리 종합용역 시행계획(안) 보고.hwx
            프로세스명: 매입임대주택 공급관리 종합용역 시행계획(안) 보고
        해결: .lstrip('0123456789-. ') # 마지막 띄어쓰기까지 해야 함.
        '''
        open_path = f'"{tmp_path}\\{fname}"'
        subprocess.Popen(open_path, shell=True)
        fname = fname.lstrip('0123456789-. ')
        if self.mp.wait_with_name(100, 0.5, fname[:10]):
            pass
        else:
            Msgbox.error(f"hwx 문서기가 켜지지 않았습니다. {open_path}, {fname[:10]}")

        #self.time.sleep(5)


    def print(self, fname):
        self.time.sleep(1)
        pa.hotkey("ctrl", "p")
        self.time.sleep(2)
        pa.press("enter")
        self.wait_print()

