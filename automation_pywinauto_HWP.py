from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import timings

# app = ( Application(backend="uia").start("notepad.exe") # .connect(title="제목 없음 - Windows 메모장", timeout=100))

# dlg = timings.wait_until_passes(
#    20, 0.5, lambda: app.window_(title="제목 없음 - Windows 메모장")
# )

# 열려있는 메모장 접근
breakpoint()
window = Desktop()["빈 문서 1 - 한컴오피스 한글 "]
"""
(Pdb) p window.print_control_identifiers()
Control Identifiers:

HwpApp : 8.0 - '빈 문서 1 - 한컴오피스 한글 '    (L0, T0, R1920, B1040)
['빈 문서 1 - 한컴오피스 한글 HwpApp : 8.0', '빈 문서 1 - 한컴오피스 한글 ', 'HwpApp : 8.0']
child_window(title="빈 문서 1 - 한컴오피스 한글 ", class_name="HwpApp : 8.0")
|
| Edit - ''    (L36, T186, R1905, B1001)
| ['빈 문서 1 - 한컴오피스 한글 Edit', 'Edit']
| child_window(class_name="HwpMainEditWnd")
"""
