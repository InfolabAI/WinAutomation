import os
from functions_timeu import TimeU
from functions_initialization import *
from functions_manage_alzip import Manage_alzip
from functions_manage_excel import Manage_excel
from functions_manage_pdf import Manage_pdf
from functions_manage_hwp import Manage_hwp
from functions_manage_hwx import Manage_hwx


class Print_files_in_a_folder:
    def __init__(self, password_list):
        self.alzip = Manage_alzip(password_list)
        self.excel = Manage_excel(password_list)
        self.pdf = Manage_pdf(password_list)
        self.hwp = Manage_hwp(password_list)
        self.hwx = Manage_hwx(password_list)
        self.time = TimeU()
        self.invalid_file_names = invalid_file_names
    
    
    def is_valid_file(self, fname):
        '''
        valid file 만 출력한다.'''
        ret = True
        for invalid_name in self.invalid_file_names:
            if invalid_name in fname:
                ret = False

        return ret
    
    def process_fname(self, fname):
        if not self.is_valid_file(fname):
            return

        #pdf 가 PDF 같이 대문자인 경우가 있어서 예외처리
        fname = fname.lower()

        #띄어쓰기 예외처리는 subprocess 구문에서 처리하고 있음.

        try:
            if ".xls" in fname or ".csv" in fname:
                self.excel.run(fname)
            if ".zip" in fname:
                self.alzip.run(fname)
            if ".pdf" in fname:
                self.pdf.run(fname)
            if ".hwp" in fname:
                self.hwp.run(fname)
        except:
            pass
    
    def process_hwx(self, fname):
        if ".hwx" in fname:
            self.hwx.run(fname)

    def print_files_in_a_folder(self, folder_path):
        
        self.time.sleep(2)
        # 본 폴더 처리
        file_list = os.listdir(folder_path)
        # 제대로 저장이 안되었다면, False
        if len(file_list) <= 1:
            return False
        
        for fname in file_list:
            self.process_hwx(fname)

        for fname in file_list:
            self.process_fname(fname)

        # 압축 풀린 폴더들 모두 처리
        file_list = os.listdir(folder_path)
        dir_list = []
        ## 폴더 모두 모으기
        for fname in file_list:
            if os.path.isdir(folder_path + "\\" + fname):
                dir_list += [fname]

        ## 모든 폴더의 파일 이름과 상대경로 모으기
        additional_file_list = []
        for dir in dir_list:
            dir_file_list = os.listdir(folder_path + "\\" + dir)
            dir_file_list = [dir + "\\" + dir_file for dir_file in dir_file_list]
            additional_file_list += dir_file_list

        ## 한번에 처리
        #for fname in additional_file_list:
        #    self.process_hwx(fname)

        for fname in additional_file_list:
            self.process_fname(fname)
        
        return True