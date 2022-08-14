import pyautogui
from functions_interface import InterfaceU
from functions_process import Manage_process


class Manage_password(InterfaceU):
    def __init__(self, timeU, password_list):
        super.__init__(timeU)
        self.mp = Manage_process(timeU)
        self.password_list = password_list
        pass

    def process_password(self, name):
        """ 모든 password_list 내 비밀번호를 비밀번호가 완료될 때까지 입력하는 함수
        Args:
            name: 비밀번호 창
        """
        if self.mp.find_element_with_name(name) is None:
            return

        for i, pw in enumerate(self.password_list):
            pyautogui.typewrite(pw)
            pyautogui.press("enter")
            print(pw)
            if self.mp.wait_once_for_process_kill_with_name(name):
                break

        while True:
            if i + 1 == len(self.password_list):
                pw = pyautogui.prompt(
                    text=f"제공된 password 들로는 현재 파일의 암호를 해제할 수 없습니다. 추가 비밀번호를 제공해주세요. 다음에는 여기에 적은 추가 비밀번호를 프로그램 실행 전에 제공해주셔야 동일한 오류가 발생하지 않습니다. 만약 이 파일을 무시하려면 아무것도 적지 않은 상태로 ok를 눌러주세요. 현재 제공된 password 는 다음과 같습니다. {str(self.password_list)}",
                    title="비밀번호 해제 오류 발생",
                )
                if pw == "":
                    break

                if self.mp.wait_once_for_process_kill_with_name(name):
                    self.password_list += [pw]
                    break

