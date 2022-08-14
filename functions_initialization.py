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
}


class Initialization:
    def __init__(self):
        ret = Msgbox.confirm(
            text="(1) 이 프로그램은 안정적인 실행을 위해 열려있는 모든 explore(인터넷), pdf, 그룹웨어 결재창, excel 문서,  한글 문서, 알집을 종료시킵니다. 저장되지 않은 문서가 있다면, 미리 저장 후 종료해주세요. \n\n(2) 이 프로그램은 압축 파일을 알집으로 해제한다고 가정합니다. 미리 알집을 설치하고, 압축 파일을 열면 알집이 사용되도록 설정해주세요. \n\n위 안내에 대한 준비가 되지 않았다면 Cancel을 눌러 종료해주시고, 준비되셨다면 OK을 눌러 진행해주세요.",
            title="안내 사항",
        )
        if ret == "Cancel":
            exit()

        os.system("mkdir " + tmp_path)
        for k, exe_name in exe_name_dict.items():
            os.system(command_kill_format + exe_name)
