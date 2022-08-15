import os
from functions_process import Manage_process
from functions_pyautogui_msgbox import Msgbox
from functions_initialization import *
from functions_interface import InterfaceU


class Manage_interface(InterfaceU):
    def __init__(self):
        super().__init__()
        self.mp = Manage_process()

    def process_kill(self):
        raise NotImplementedError()

    def run(self, fname):
        """
        전체 실행을 담당한다"""
        raise NotImplementedError()

    def password_cycle(self, fname):
        """
        password list 의 모든 password 를 처리함
        """
        while self.pw.password_start_check():
            ret = Msgbox.file_reopen(text="파일에 암호가 걸려있습니다. 올바른 암호를 입력한 후, 이 창의 암호 입력 완료 버튼을 눌러주세요. \n\n만약 암호 입력에 에러가 발생했다면, 파일 다시 열기 버튼를 눌러 파일을 새로 열고 암호를 입력한 후, 이 창의 암호 입력 완료 버튼을 눌러주세요.", title="암호 입력 필요")
            if ret:
                self.process_kill()
                self.time.sleep(2)
                self.process(fname)
            
        # password 입력 창이 없으면 자동 종료.
        #if self.pw.password_start_check():
        #    for i, pw in enumerate(self.pw.password_list):
        #        if self.pw.password_once(pw):
        #            break
        #        else:
        #            # password 가 틀리면, 모두 종료하고, 폴더 파일 지우고, 처음부터 다시 함
        #            self.process_kill()
        #            self.process(fname)

        #    if i + 1 == len(self.pw.password_list):
        #        # 제공된 모든 비번이 제대로 동작하지 않을 때를 처리
        #        while True:
        #            self.time.sleep(1)
        #            pw = self.pw.password_list_failed()
        #            if self.pw.password_once(pw):
        #                self.pw.password_list += [pw]
        #                break
        #            else:
        #                # password 가 틀리면, 모두 종료하고, 폴더 파일 지우고, 처음부터 다시 함
        #                self.process_kill()
        #                self.process(fname)

    def process(self, fname):
        """
        Args:
            fname: 압축해제를 수행할 파일의 이름"""
        raise NotImplementedError()

    def wait_print(self):
        self.mp.wait_with_name(10,0.5,"인쇄")
        self.mp.wait_kill_with_name(10,0.5,"인쇄")
        self.time.sleep(1)
        