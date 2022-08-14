import pyautogui as pa
import os
from functions_interface import InterfaceU
from functions_process import Manage_process
from functions_initialization import *


class Manage_saving(InterfaceU):
    def __init__(self):
        super().__init__()
        self.mp = Manage_process()

    def saving_files_in_one_paper(self, process_el):
        """
        하나의 게시글의 모든 파일을 저장하는 함수

        Args:
            name: 게시글의 이름 (예., 지출결의서 - 평택고덕단지)
        """
        window = self.mp.open_window_with_handle(process_el.handle)

        window.ToolBar.저장Button.click()
        os.system(command_del_tmp)

        self.mp.wait_for_process_open_with_name("다른 이름으로")
        pa.hotkey("ctrl", "l")
        pa.typewrite(tmp_path)
        pa.press("enter")
        pa.hotkey("alt", "s")

        self.time.sleep(3)
        os.system(command_kill_format + exe_name_dict["groupware"])
        self.time.sleep(1)
