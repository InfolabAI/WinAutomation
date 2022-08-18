import os
import pyautogui
from functions_initialization import *
from functions_pyautogui_msgbox import Msgbox
'''
프로세스마다 특성값 정리
0. 노하우
- 하나의 프로그램에서 다수의 창 (e.g., 인쇄 등)이 떠도, Application().connect(class_name=<프로그램의 class_name (e.g., ALZipClass)>) 으로 통일.
- 예외적으로 알집은, 메인 화면에서 다수의 print_ctrl_ids() 등의 접근을 막아놔서 <빠르게 압축풀기> 창을 따로 찾아야 함
- 내부 정보에 접근할 때는, 가능하다면 window spy 의 Text 를 통해 접근. ClassNN 은 숫자가 맞지 않는 경우가 많음 (e.g., Combobox4 라고 했는데 알고보니 Combobox3)
- Combobox select 방법
    - Combobox1.type_keys("%{DOWN}").select("Canon Printer Driver").type_keys("%{ENTER}")
- 에러: Neither GUI element (wrapper) nor wrapper method
    - uia에 없는 객체를 다루면 get_toggle_state() 등을 위 에러로 사용할 수 없음.
    - 해결방법: wrapper_object() 를 사용한다.
    - dir 사용방법: dir(window.wrpper_object()) 하면 모든 사용가능한 함수가 나온다.
    - Checkbox 다루는 법: check(), uncheck(), get_check_state()
    - hyperlink 클릭: aa['프린터 속성Hyperlink'].wrapper_object().invoke()

1. alzip
class_name (title): ALZipClass (...알집)
압축풀기버튼: XTPToolBar1

압축 풀기 창 class_name (title): #32770 (빠르게 압축풀기)
선택된 폴더 하위에..: Button1
압축풀기 후 폴더열기: Button4

비밀번호 입력 창 class_name (title): #32770 (비밀번호 입력)
입력박스: Edit2

비밀번호 틀렸을 때의 창 class_name (title):

2. Foxit
class_name (title): classFoxitPhantom (...Foxit PhantomPDF)

비밀번호 입력 창 class_name (title): #32770 (암호)
입력박스: Edit1

비밀번호 틀렸을 때의 창 class_name (title): #32770 (Foxit PhantomPDF)
    ClassNN:	Static1
    Text:	잘못된 암호를 입력했습니다. 암호를 다시 입력하십시오.

인쇄 창 class_name (title): #32770 (인쇄)
    ClassNN:	Button21
    Text:	한 면에 여러  (...)

    ClassNN:	ComboBox1
    Text:	Canon Printer Driver

    ClassNN:	ComboBox4
    Text:	사용자 정의, 2, 4 등등 포함

3. excel
class_name (title): 
    ahk_class XLMAIN
    ahk_exe EXCEL.EXE

비밀번호 입력 창 class_name (title): 
    암호
    ahk_class bosa_sdm_XL9
입력박스: 
    ClassNN:	EDTBX1

비밀번호 틀렸을 때의 창 class_name (title):
    Microsoft Excel
    ahk_class #32770

    ClassNN:	Static2
    Text:	암호가 잘못되었습니다. <Caps Lock> 키가 꺼져 있는지, 대소문자 (...)

인쇄 창
    창과 버튼들을 class 객체로 다룰 수 없음. (단축키만 쳐야할 듯)
    프린터 속성으로 들어가서 다룰 수는 있을 듯.
    ctrl+p > NetUIHWND1 가 떴는지 확인하고 엔터.

4. hwp
class_name (title): 
    ... - 한컴오피스 한글
    ahk_class HwpApp : 9.0
    ahk_exe Hwp.exe

비밀번호 입력 창 class_name (title): 
    문서 암호
    ahk_class HNC_DIALOG
입력박스: 
    control 로 다룰 수 없음

비밀번호 틀렸을 때의 창 class_name (title):
    한글
    ahk_class HNC_DIALOG

인쇄
    인쇄
    ahk_class HNC_DIALOG

5. hwx
class_name (title): 
    ... - 한컴오피스 한글
    ahk_class HwpApp : 9.0
    ahk_exe Hwp.exe

인쇄
    인쇄

6. groupware
class_name (title): 
pc저장버튼: 

'''
#valid_file_names = [ "명세", "견적", "매출", "청구", "증빙", "통장", "보고", "명단", "요청", "확인", "영수", "조서", "검사", "기성", "증명", "사진", "고지", "선금", "이행", "계약", "소유", "등기", "대장", "계산", "정산", "료", "약정", "계좌", "집행", "지출", "내역"]
invalid_file_names = ["평가서", "회보", "일계"]

tmp_env = os.environ["TEMP"]
tmp_path = tmp_env + "\\pyauto"
command_del_format = "del /q /s /f " + tmp_path + "\\"
command_rd_tmp = "rd /q /s " + tmp_path + "\\"
command_kill_format = "taskkill /f /im "
exe_name_dict = {
    "alzip": "Alzip.exe",
    "alzip_residual": "auirender.exe",
    "hwx": "XSViewer.exe",
    "hwp": "Hwp.exe",
    "groupware": "SaViewX.exe",
    "ie": "iexplore.exe",
    "excel": "excel.exe",
    "pdf": "FoxitPhantomPDF.exe",
}


class Initialization:
    def __init__(self):
        ret = Msgbox.confirm(
            text="(1) 이 프로그램은 안정적인 실행을 위해 열려있는 모든 explore(인터넷), pdf, 그룹웨어 결재창, excel 문서,  한글 문서, 알집을 종료시킵니다. 저장되지 않은 문서가 있다면, 미리 저장 후 종료해주세요. \n\n(2) 이 프로그램은 Foxit(pdf), 알집(압축 파일)을 사용한다고 가정합니다. 사용 전에 두 프로그램을 사용하도록 설정해주세요. \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주세요.",
            title="안내 사항",
        )
        if ret == False:
            exit()

        ret = Msgbox.confirm(
            #text="진행 중에 비밀번호가 걸린 파일을 만나면 사용자가 비밀번호를 입력해야 합니다. 추후 추가 기능으로 비밀번호 자동 입력 기능을 개발할수도 있습니다. \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주세요.",
            text="진행 중에 비밀번호가 걸린 파일을 만나면 출력 없이 지나갑니다. 추후 추가 기능으로 비밀번호 자동 입력 기능을 개발할수도 있습니다. \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주세요.",
            title="안내 사항",
        )
        if ret == False:
            exit()

        ret = Msgbox.confirm(
            text="모든 문서 프로그램의 인쇄경로는 사전에 canon printer driver로 설정되어 있어야 합니다. Excel은 항상 '한페이지에 모든 열 맞추기'로 출력합니다. \n\n만약 프린터에 인쇄물을 보내지 않고 테스트를 해보시려면, window키 → 프린터 및 스캐너 검색 → canon printer driver 대기열 열기 → 프린터(P) → 오프라인으로 프린터 사용 을 켜주시기 바랍니다. \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주세요.",
            title="안내 사항",
        )
        if ret == False:
            exit()

        ret = Msgbox.confirm(
            text=f"이 프로그램은 아래 단어를 포함하지 않는 첨부 문서만 인쇄합니다. 증빙에 불필요한 자료를 제외하여 자원을 절약하기 위함입니다. 추가가 필요하면 말씀해주세요. \n\n{str(invalid_file_names)} \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주세요.",
            title="안내 사항",
        )
        if ret == False:
            exit()

        self.skip_num = Msgbox.prompt(
            text=f"인쇄하지 않고 넘길 문서 갯수를 입력해주세요. 입력하지 않으면 문서를 넘기지 않습니다.",
            title="안내 사항",
        )
        if self.skip_num == '':
            self.skip_num = '0'

        self.password = ['11']
        #password = Msgbox.prompt(
        #    text="인쇄 진행 중 암호가 걸린 파일을 만났을 때 시도할 암호 리스트를 입력해주세요. 입력한 암호들을 순서대로 적용합니다. \n\n예를 들어, 사용하는 암호가 0982! 와 2832@ 두 개라면, 아래 예와 같이 입력하면 됩니다. 세 개 이상이어도 동일한 규칙으로 적으시면 됩니다. 이 양식을 지키지 않으면 오류가 발생합니다. \n\n각 암호를 구분하는 기호는 , (쉼표) 입니다. \n\n예) \n0982!,2832@",
        #    title="안내 사항",
        #)
        #if password is None:
        #    exit()

        #password = password.replace(" ", "").split(",")
        #self.password = password

        #ret = Msgbox.confirm(
        #    text=f"입력한 암호 리스트는 다음과 같습니다. 의도와 다른 값이라면 Cancel을 눌러 종료해주세요. \n\n{str(password)}",
        #    title="입력한 암호 확인",
        #)
        #if ret == False:
        #    exit()

        for k, exe_name in exe_name_dict.items():
            os.system(command_kill_format + exe_name)
