import os
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
    
    def process_fname(self, fname):
        if ".xls" in fname or ".csv" in fname:
            self.excel.run(fname)
        if ".zip" in fname:
            self.alzip.run(fname)
        if ".pdf" in fname:
            self.pdf.run(fname)
        if ".hwp" in fname:
            self.hwp.run(fname)
    
    def process_hwx(self, fname):
        if ".hwx" in fname:
            self.hwx.run(fname)

    def print_files_in_a_folder(self, folder_path):
        # 본 폴더 처리
        file_list = os.listdir(folder_path)
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
        for fname in additional_file_list:
            self.process_fname(fname)