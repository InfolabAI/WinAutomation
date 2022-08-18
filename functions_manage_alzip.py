import subprocess
import pyautogui as pa
import os
from functions_pyautogui_msgbox import Msgbox
from functions_initialization import *
from functions_manage_interface import Manage_interface
from functions_password_alzip import Password_alzip


class Manage_alzip(Manage_interface):
    def __init__(self, password_list):
        super().__init__()
        self.pw = Password_alzip(password_list)

    def run(self, fname):
        self.process_kill()
        self.process(fname)
        self.password_cycle(fname)
        self.time.sleep(3)
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
        os.system(command_del_format + f'"{self.folder_name_for_rm}"')
        os.system(command_del_format + f'"{self.folder_name_for_rm + "$ENC$"}"')

        self.is_process_open(fname, "ALZipClass")

        # 메인 화면에서 control 접근 시 알집이 꺼지는 에러가 발생하는 것을 확인해서 단축키로 함
        self.time.sleep(0.5)
        pa.hotkey('ctrl', 'e')

        # 압축풀기가 켜졌는지 확인
        if self.mp.wait_with_name(50, 0.5, "빠르게"):
            pass
        else:
            Msgbox.error("압축 풀기 창이 켜지지 않았습니다.")


        # 메인 화면에서 control 접근 시 알집이 꺼지는 에러가 발생하는 것을 확인해서 <빠르게 압축풀기> window를 따로 찾음
        window = self.mp.open_window_with_name("빠르게 압축풀기")
        pa.typewrite(tmp_path)

        cont1 = self.mp.find_control(window, 'Checkbox', '선택된 폴더')[0].wrapper_object()
        cont2 = self.mp.find_control(window, 'Checkbox', '압축풀기 후 폴더')[0].wrapper_object()

        # 선택된 폴더 하위에 압축파일명으로 폴더 생성(F) 의 상태 확인 후 켜기
        while cont1.get_check_state() == 0:
            cont1.check()
            self.time.sleep(1)
        while cont2.get_check_state() == 1:
            cont2.uncheck()
            self.time.sleep(1)

        pa.press("enter")

