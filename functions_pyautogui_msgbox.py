import pyautogui
import easygui


class Msgbox:
    def __init__(self):
        pass

    @classmethod
    def alert(self, text, title):
        # return pyautogui.alert(text=text, title=title, button="OK")
        return easygui.msgbox(msg=text, title=title, ok_button="OK")

    @classmethod
    def confirm(self, text, title):
        # return pyautogui.confirm(text=text, title=title, buttons=("OK", "Cancel"))
        return easygui.ynbox(
            msg=text, title=title, choices=["OK", "Cancel"]
        )  # return: True or False

    @classmethod
    def prompt(self, text, title):
        # return pyautogui.prompt(text=text, title=title)
        return easygui.enterbox(msg=text, title=title)  # return: value or None
