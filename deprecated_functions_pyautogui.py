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


"""
https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

locateOnScreen(image, grayscale=False) - Returns (left, top, width, height) coordinate of first found instance of the image on the screen. Raises ImageNotFoundException if not found on the screen.

locateCenterOnScreen(image, grayscale=False) - Returns (x, y) coordinates of the center of the first found instance of the image on the screen. Raises ImageNotFoundException if not found on the screen.

locateAllOnScreen(image, grayscale=False) - Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen.

locate(needleImage, haystackImage, grayscale=False) - Returns (left, top, width, height) coordinate of first found instance of needleImage in haystackImage. Raises ImageNotFoundException if not found on the screen.

locateAll(needleImage, haystackImage, grayscale=False) - Returns a generator that yields (left, top, width, height) tuples for where needleImage is found in haystackImage.

"""
