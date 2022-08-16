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
        # 그룹웨어는 uia 를 켜지 않으면, 완전히 다른 메뉴를 가지기 때문에 저장 버튼을 누를 수 없음. uia 로 켤때, 찾을 수 없다는 에러가 나면 해당 창을 한 번 클릭해주면 그 다음은 찾을 수 있음.
        window = self.mp.open_window_with_handle(process_el.handle, uia=True)

        window.저장Button.wrapper_object().click()
        os.system(command_rd_tmp)
        self.time.sleep(1)
        os.system("mkdir " + tmp_path)

        self.mp.wait_for_process_open_with_name("다른 이름으로")
        self.time.sleep(0.1)
        pa.hotkey("ctrl", "l")
        self.time.sleep(0.1)
        pa.typewrite(tmp_path)
        self.time.sleep(0.1)
        pa.press("enter")
        self.time.sleep(0.1)
        pa.hotkey("alt", "s")

        self.time.sleep(5)
        # 결재정보를 저장하고 있다는 창 이름이 '알림'이다.
        self.mp.wait_kill_with_name(10,0.5,"알림")
        os.system(command_kill_format + exe_name_dict["groupware"])
        self.time.sleep(1)
