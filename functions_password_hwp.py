import pyautogui
from functions_password_interface import Password_interface


class Password_hwp(Password_interface):
    def __init__(self, password_list):
        super().__init__("문서 암호", password_list)
        self.password_error_name = "한글"

    def password_once(self, password):
        # 비밀번호 Edit window 에 focus 하기
        self.mp.wait_with_name(10, 0.1, self.name)
        window = self.mp.open_window_with_name(self.name)

        ## Window 마다 path 가 다른 부분
        window.EditBX1.set_focus()

        # 비밀번호 작성하기
        pyautogui.typewrite(password)
        pyautogui.press("enter")
        return self.password_check()

    def password_check(self):
        if self.mp.wait_once_for_process_open_with_name(self.password_error_name):
        #if self.mp.wait_with_class_name(2, 0.2, "bosa_sdm_XL9"):
            # password 에러 창이 실행 중이면 password 가 틀린 것이므로 False
            return False
        else:
            return True
