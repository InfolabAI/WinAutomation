import pyautogui
from functions_password_interface import Password_interface


class Password_alzip(Password_interface):
    def __init__(self, password_list):
        super().__init__("비밀번호 입력", password_list)

    def password_once(self, password):
        # 비밀번호 Edit window 에 focus 하기
        process_el = self.mp.find_element_with_name(self.name)
        window = self.mp.open_window_with_handle(process_el.handle)

        ## Window 마다 path 가 다른 부분
        window.Edit2.set_focus()

        # 비밀번호 작성하기
        self.time.sleep(0.5)
        pyautogui.typewrite(password)
        pyautogui.press("enter")
        return self.password_check()

    def password_check(self):
        if self.mp.wait_once_for_process_open_with_name(self.name):
            # 동일한 비번 창이 실행 중이면 password 가 틀린 것이므로 False
            return False
        else:
            return True
