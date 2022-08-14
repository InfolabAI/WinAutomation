import os
from functions_initialization import *
from functions_interface import InterfaceU


class Manage_interface(InterfaceU):
    def __init__(self):
        super().__init__()

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
        # password 입력 창이 없으면 자동 종료.
        if self.pw.password_start_check():
            for i, pw in enumerate(self.pw.password_list):
                if self.pw.password_once(pw):
                    break
                else:
                    # password 가 틀리면, 모두 종료하고, 폴더 파일 지우고, 처음부터 다시 함
                    self.process_kill()
                    self.process(fname)

            if i + 1 == len(self.pw.password_list):
                # 제공된 모든 비번이 제대로 동작하지 않을 때를 처리
                while True:
                    self.time.sleep(1)
                    pw = self.pw.password_list_failed()
                    if self.pw.password_once(pw):
                        self.pw.password_list += [pw]
                        break
                    else:
                        # password 가 틀리면, 모두 종료하고, 폴더 파일 지우고, 처음부터 다시 함
                        self.process_kill()
                        self.process(fname)

    def process(self, fname):
        """
        Args:
            fname: 압축해제를 수행할 파일의 이름"""
        raise NotImplementedError()
