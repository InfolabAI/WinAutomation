import pywinauto
import pyautogui as pa
import time
import pyautogui
from pywinauto.application import Application
from email.mime import application

capture_path = "C:\\Users\\HC\\OneDrive\\ICE\\capture\\"



def locateOnScreen(file_name, path=capture_path):
    num = pa.locateOnScreen(capture_path + file_name)
    if num is None:
        pa.alert(text="", title="이미지가 화면에 없습니다.", button="OK")
        exit(0)
    return num

def open_window_with_handle(handle):
    # found_index 0는 pywinauto.findwindows.ElementAmbiguousError 를 없애기 위해 사용.
    return Application("uia").connect(handle=handle).window(found_index=0)

def save_files_with_window(window):
    """
    window 를 이용해서 file 을 저장함
    """
    window.ToolBar.저장Button.click()
    # window.Pane1.ComboBox2.열기.click()
    # print(window.Pane1.ComboBox2.print_config_identifier())



"""
https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

locateOnScreen(image, grayscale=False) - Returns (left, top, width, height) coordinate of first found instance of the image on the screen. Raises ImageNotFoundException if not found on the screen.

locateCenterOnScreen(image, grayscale=False) - Returns (x, y) coordinates of the center of the first found instance of the image on the screen. Raises ImageNotFoundException if not found on the screen.

locateAllOnScreen(image, grayscale=False) - Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen.

locate(needleImage, haystackImage, grayscale=False) - Returns (left, top, width, height) coordinate of first found instance of needleImage in haystackImage. Raises ImageNotFoundException if not found on the screen.

locateAll(needleImage, haystackImage, grayscale=False) - Returns a generator that yields (left, top, width, height) tuples for where needleImage is found in haystackImage.

"""
