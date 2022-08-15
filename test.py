import pywinauto
import pyautogui as pa
import time
from pprint import pprint
from functions_process import Manage_process

mp = Manage_process()
class_name = "XLMAIN"
pprint(pywinauto.findwindows.find_elements(class_name=class_name))
window = pywinauto.Application('uia').connect(found_index=0, class_name=class_name).window(found_index=0)
#window = pywinauto.Application('uia').connect(found_index=0, title="평택고덕 서정리역 단지 내 일반상가(근린생활시설) 세부운영협약 체결완료").window(found_index=0)
if '현재 설정된 용지' in window['크기조정ComboBox'].wrapper_object().selected_text():
    window['크기조정ComboBox'].wrapper_object().expand()
    time.sleep(1)
    pa.press('down', 2)
    pa.press('enter')
if '한 페이지에 시트' in window['크기조정ComboBox'].wrapper_object().selected_text():
    window['크기조정ComboBox'].wrapper_object().expand()
    time.sleep(1)
    pa.press('down', 1)
    pa.press('enter')
if '한 페이지에 모든 행' in window['크기조정ComboBox'].wrapper_object().selected_text():
    window['크기조정ComboBox'].wrapper_object().expand()
    time.sleep(1)
    pa.press('up', 1)
    pa.press('enter')

quit()

print(mp.find_control(window=window, class_type="Checkbox", sub_text="선택"))