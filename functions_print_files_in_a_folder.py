import os
from functions_manage_alzip import Manage_alzip
from functions_manage_excel import Manage_excel


class Print_files_in_a_folder:
    def __init__(self, password_list):
        self.alzip = Manage_alzip(password_list)
        self.excel = Manage_excel(password_list)

    def print_files_in_a_folder(self, folder_path):
        file_list = os.listdir(folder_path)
        for fname in file_list:
            if ".xls" in fname or ".csv" in fname:
                self.excel.run(fname)
            # if ".zip" in fname:
            #    self.alzip.run(fname)
