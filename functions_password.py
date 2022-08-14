import pyautogui
from functions_pyautogui_msgbox import Msgbox
from functions_interface import InterfaceU
from functions_process import Manage_process


class Manage_password(InterfaceU):
    def __init__(self, password_list):
        super().__init__()
        self.mp = Manage_process()
        self.password_list = password_list
        pass

    def password_excel(self, password):
        """
        password 를 한번 입력했을 때를 처리한다. check까지 담당함."""

    def password_excel_check(self):
        """
        비밀번호 틀렸는지를 확인하고, 맞았으면 True, 틀렸으면 False를 return함"""
        # 비밀번호 틀렸을 때 확인
        process_el = self.mp.wait_for_process_open_with_name("Microsoft Excel")
        window = self.mp.open_window_with_handle(process_el.handle)

        # 정리> Text, Combobox 등의 text를 가져온다.
        if "암호가 잘못" in window()["Static1"].window_text():
            return False
        else:
            return True
