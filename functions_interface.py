from functions_timeu import TimeU
from functions_pyautogui_msgbox import Msgbox


class InterfaceU:
    def __init__(self):
        self.time = TimeU()

    def raise_error(self, text):
        Msgbox.alert(text=text, title="오류 발생")
        raise Exception()

