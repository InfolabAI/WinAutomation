from functions_pyautogui_msgbox import Msgbox
from functions_process import Manage_process
from functions_interface import InterfaceU


class Password_interface(InterfaceU):
    def __init__(self, name, password_list):
        """
        Args:
            name: password 창을 구별하는 이름
            password_list: 시도할 password list"""
        super().__init__()
        self.name = name
        self.password_list = password_list
        self.mp = Manage_process()

    def password_once(self, password):
        """
        password 를 한번 입력했을 때를 처리
        
        check까지 담당함"""
        raise NotImplementedError()

    def password_start_check(self):
        """
        password 가 걸려있고, 입력창이 떴으면 True 없으면 False"""
        # 파일 이름에 '암호' 라는 말이 있을 경우, 암호 창의 '암호'와 모호해짐. 그래서 정확한 이름으로 진행
        return self.mp.wait_with_exact_name(3,0.2, self.name)

    def password_check(self):
        """
        password 가 맞았는지 check"""
        raise NotImplementedError()

    def password_list_failed(self):
        """
        password list 가 틀렸을 때 pw 추가"""
        pw = Msgbox.prompt(
            text=f"제공된 password 들로는 현재 파일의 암호를 해제할 수 없습니다. 추가 비밀번호를 입력하고 OK를 눌러주세요. 다음에는 여기에 적은 추가 비밀번호를 프로그램 실행 전에 제공해주셔야 동일한 오류가 발생하지 않습니다. \n\n만약 현재 파일을 무시하려면 Cancel을 눌러주세요. \n\n현재 제공된 password 는 다음과 같습니다. {str(self.password_list)}",
            title="비밀번호 해제 오류 발생",
        )
        # Cancel 누르면, pw 는 None 이 됨
        return pw
