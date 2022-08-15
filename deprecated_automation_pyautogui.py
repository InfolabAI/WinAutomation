import pyautogui as pa
from functions import *

# pip install pyautogui
# pip install opencv-python

print(pa.position())
num = locateOnScreen("7.jpg")

print(num)

pa.click(num, clicks=3, interval=0.25)

