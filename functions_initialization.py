import os
import pyautogui
from functions_pyautogui_msgbox import Msgbox

tmp_env = os.environ["TEMP"]
tmp_path = tmp_env + "\\pyauto"
command_del_format = "del /q /s /f " + tmp_path + "\\"
command_del_tmp = command_del_format + "*"
command_kill_format = "taskkill /f /im "
exe_name_dict = {
    "alzip": "Alzip.exe",
    "alzip_residual": "auirender.exe",
    "hwx": "XSViewer.exe",
    "groupware": "SaViewX.exe",
    "ie": "iexplore.exe",
    "excel": "excel.exe",
    "pdf": "FoxitPDFReader.exe",
}


class Initialization:
    def __init__(self):
        ret = Msgbox.confirm(
            text="(1) 이 프로그램은 안정적인 실행을 위해 열려있는 모든 explore(인터넷), pdf, 그룹웨어 결재창, excel 문서,  한글 문서, 알집을 종료시킵니다. 저장되지 않은 문서가 있다면, 미리 저장 후 종료해주세요. \n\n(2) 이 프로그램은 Foxit(pdf), 알집(압축 파일)을 사용한다고 가정합니다. 사용 전에 두 프로그램을 사용하도록 설정해주세요. \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주세요.",
            title="안내 사항",
        )
        if ret == False:
            exit()

        password = Msgbox.prompt(
            text="인쇄 진행 중 암호가 걸린 파일을 만났을 때 시도할 암호 리스트를 입력해주세요. 입력한 암호들을 순서대로 적용합니다. \n\n예를 들어, 사용하는 암호가 0982! 와 2832@ 두 개라면, 아래 예와 같이 입력하면 됩니다. 세 개 이상이어도 동일한 규칙으로 적으시면 됩니다. 이 양식을 지키지 않으면 오류가 발생합니다. \n\n각 암호를 구분하는 기호는 , (쉼표) 입니다. \n\n예) \n0982!,2832@",
            title="안내 사항",
        )
        if password is None:
            exit()

        password = password.replace(" ", "").split(",")
        self.password = password

        ret = Msgbox.confirm(
            text=f"입력한 암호 리스트는 다음과 같습니다. 의도와 다른 값이라면 Cancel을 눌러 종료해주세요. \n\n{str(password)}",
            title="입력한 암호 확인",
        )
        if ret == False:
            exit()

        os.system("mkdir " + tmp_path)
        for k, exe_name in exe_name_dict.items():
            os.system(command_kill_format + exe_name)
