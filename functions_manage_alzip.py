import subprocess
import pyautogui as pa
import os
from functions_initialization import *
from functions_process import Manage_process
from functions_manage_interface import Manage_interface
from functions_saving_a_paper import Manage_saving
from functions_password_alzip import Password_alzip


class Manage_alzip(Manage_interface):
    def __init__(self, password_list):
        super().__init__()
        self.mp = Manage_process()
        self.pw = Password_alzip(password_list)

    def run(self, fname):
        self.process_kill()
        self.process(fname)
        self.password_cycle(fname)
        self.process_kill()

    def process_kill(self):
        os.system(command_kill_format + exe_name_dict["alzip"])
        os.system(command_kill_format + exe_name_dict["alzip_residual"])

    def process(self, fname):
        """
        Args:
            fname: 압축해제를 수행할 파일의 이름"""
        # 압축해제된 폴더 삭제를 위한 경로 설정
        self.folder_name_for_rm = fname.split(".zip")[0]
        os.system(command_del_format + self.folder_name_for_rm)

        # 띄어쓰기 문제 해결 및 경로 문제 해결
        subprocess.Popen(f'"{tmp_path}\\{fname}"', shell=True)
        process_el = self.mp.wait_for_process_open_with_name(fname[:10])
        window = self.mp.open_window_with_handle(process_el.handle)
        window.압축풀기Button.click()
        process_el_sub = self.mp.wait_for_process_open_with_name("압축풀기")
        window_sub = self.mp.open_window_with_handle(process_el_sub.handle)
        pa.typewrite(tmp_path)
        # 선택된 폴더 하위에 압축파일명으로 폴더 생성(F) 의 상태 확인 후 켜기
        while window_sub["선택된 폴더 하위에 압축파일명으로 폴더 생성"].get_toggle_state() == 0:
            window_sub["선택된 폴더 하위에 압축파일명으로 폴더 생성"].click()
            self.time.sleep(0.1)
        while window_sub["압축풀기 후 폴더열기"].get_toggle_state() == 1:
            window_sub["압축풀기 후 폴더열기"].click()
            self.time.sleep(0.1)
        pa.press("enter")

        self.time.sleep(3)
