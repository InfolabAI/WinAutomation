import pyautogui


class InterfaceU:
    def __init__(self, timeU):
        self.time = timeU

    def raise_error(self, text):
        pyautogui.alert(text=text, title="오류 발생")
        raise Exception()

