import pyautogui


class Msgbox:
    def __init__(self):
        pass

    @classmethod
    def alert(self, text, title):
        return pyautogui.alert(text=text, title=title, button="OK")

    @classmethod
    def confirm(self, text, title):
        return pyautogui.confirm(text=text, title=title, buttons=("OK", "Cancel"))

    @classmethod
    def prompt(self, text, title):
        return pyautogui.prompt(text=text, title=title)
