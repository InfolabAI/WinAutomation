from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import timings

# app = ( Application(backend="uia").start("notepad.exe") # .connect(title="제목 없음 - Windows 메모장", timeout=100))

# dlg = timings.wait_until_passes(
#    20, 0.5, lambda: app.window_(title="제목 없음 - Windows 메모장")
# )

# 열려있는 메모장 접근
dlg = Application("uia").connect(title="제목 없음 - Windows 메모장")
# 메모장 window에서 스크롤바 클릭하기
dlg.window()["Edit -> ScrollBar"].아래쪽_스크롤_화살표.click()
# 메모장 window에서 스크롤바 클릭하기 V2
dlg.window()["Edit"].세로.아래쪽_스크롤_화살표.click()
# 규칙: list 안에 있는 이름으로 접근해야 함.
# e.g., ['Edit'], ['세로', 'ScrollBar', '세로ScrollBar'] ...

"""
(Pdb) p dlg.window().print_control_identifiers()
Control Identifiers:

Dialog - '제목 없음 - Windows 메모장'    (L280, T236, R888, B797)
['제목 없음 - Windows 메모장', '제목 없음 - Windows 메모장Dialog', 'Dialog']
child_window(title="제목 없음 - Windows 메모장", control_type="Window")
|
| Edit - '텍스트 편집'    (L288, T287, R880, B767)
| ['Edit']
| child_window(title="텍스트 편집", auto_id="15", control_type="Edit")
|    | 
|    | ScrollBar - '세로'    (L863, T287, R880, B767)
|    | ['세로', 'ScrollBar', '세로ScrollBar]
|    | child_window(title="세로", auto_id="NonClientVerticalScrollBar", control_type="ScrollBar")
|    |    |
|    |    | Button - '위쪽 스크롤 화살표'    (L863, T287, R880, B304)
|    |    | ['위쪽 스크롤 화살표', 'Button', '위쪽 스크롤 화살표Button', 'Button0', 'Button1']
|    |    | child_window(title="위쪽 스크롤 화살표", auto_id="UpButton", control_type="Button")
|    |    |
|    |    | Button - '아래쪽 스크롤 화살표'    (L863, T750, R880, B767)
|    |    | ['아래쪽 스크롤 화살표Button', 'Button2', '아래쪽 스크롤 화살표']
|    |    | child_window(title="아래쪽 스크롤 화살표", auto_id="DownButton", control_type="Button")
|
| StatusBar - '상태 표시줄'    (L288, T767, R880, B789)
| ['StatusBar', '상태 표시줄StatusBar', '상태 표시줄']
| child_window(title="상태 표시줄", auto_id="1025", control_type="StatusBar")
|    | 
|    | Static - ''    (L288, T769, R450, B789)
|    | ['Static', 'Static0', 'Static1']
|    |
|    | Static - '  Ln 1, Col 1'    (L452, T769, R590, B789)
|    | ['Static2', '  Ln 1, Col 1', '  Ln 1, Col 1Static']
|    | child_window(title="  Ln 1, Col 1", control_type="Text")
|    | 
|    | Static - ' 100%'    (L592, T769, R640, B789)
|    | [' 100%Static', 'Static3', ' 100%']
|    | child_window(title=" 100%", control_type="Text")
|    |
|    | Static - ' Windows (CRLF)'    (L642, T769, R760, B789)
|    | ['Static4', ' Windows (CRLF)Static', ' Windows (CRLF)']
|    | child_window(title=" Windows (CRLF)", control_type="Text")
|    | 
|    | Static - ' UTF-8'    (L762, T769, R864, B789)
|    | [' UTF-8', ' UTF-8Static', 'Static5']
|    | child_window(title=" UTF-8", control_type="Text")
|
| TitleBar - ''    (L304, T239, R880, B267)
| ['TitleBar']
|    | Menu - '시스템'    (L288, T244, R310, B266)
|    | child_window(title="시스템", auto_id="MenuBar", control_type="MenuBar")
|    |    |
|    |    | MenuItem - '시스템'    (L288, T244, R310, B266)
|    |    | ['시스템MenuItem', 'MenuItem', '시스템2', 'MenuItem0', 'MenuItem1']
|    |    | child_window(title="시스템", control_type="MenuItem")
|    |
|    | ['최소화', 'Button3', '최소화Button']
|    | child_window(title="최소화", control_type="Button")
|    |
|    | Button - '최대화'    (L788, T237, R834, B267)
|    | ['최대화', 'Button4', '최대화Button']
|    | child_window(title="최대화", control_type="Button")
|    | Button - '닫기'    (L834, T237, R881, B267)
|    | child_window(title="닫기", control_type="Button")
| Menu - '응용 프로그램'    (L288, T267, R880, B286)
| child_window(title="응용 프로그램", auto_id="MenuBar", control_type="MenuBar")
|    |
|    | ['파일(F)MenuItem', 'MenuItem2', '파일(F)']
|    |
|    | ['편집(E)', 'MenuItem3', '편집(E)MenuItem']
|    |
|    | MenuItem - '서식(O)'    (L392, T267, R447, B286)
|    | ['서식(O)MenuItem', 'MenuItem4', '서식(O)']
|    | child_window(title="서식(O)", control_type="MenuItem")
|    |
|    | MenuItem - '보기(V)'    (L447, T267, R501, B286)
|    | child_window(title="보기(V)", control_type="MenuItem")
|    | MenuItem - '도움말(H)'    (L501, T267, R568, B286)
|    | child_window(title="도움말(H)", control_type="MenuItem")
"""

# 원하는 이름을 가진 창 찾기 (아직 미완성)
windows = Desktop(backend="uia").windows()
for ww in windows:
    if "메모장" in ww.window_text():
        name = ww.window_text()
        print(ww)
        breakpoint()
        app = Desktop(backend="uia").window(best_match=name)
        print(app.print_control_identifiers())

"""
(Pdb) p windows
[<uiawrapper.UIAWrapper - '작업 표시줄', Pane, -2039402811>, <uiawrapper.UIAWrapper - '', Pane, -158898699>, <uiawrapper.UIAWrapper - '제목 없음 - Windows 메모장', Dialog, -1667884694>, ...]
(Pdb) p windows[2]
<uiawrapper.UIAWrapper - '제목 없음 - Windows 메모장', Dialog, -1667884694>
(Pdb) p windows[2].maximize()
<uiawrapper.UIAWrapper - '제목 없음 - Windows 메모장', Dialog, -1667884694>
"""

breakpoint()
app.UntitledNotepad.print_control_identifiers()

