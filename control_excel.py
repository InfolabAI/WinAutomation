import pandas as  pd
import openpyxl as op
import win32com.client
import os

'''
다수의 excel 파일에서 원하는 시트, 원하는 열만 가져와서 합치는 코드
'''
main_path = 'D:\\문서 모음\\행복주택 현황 (박시우 대리님)\\수기계약자리스트\\'

file_list = os.listdir(main_path)

xlApp = win32com.client.Dispatch("Excel.Application")

df_concat = None
for file_ in file_list:
    '''
    [동, 모집회차, 세부타입, 계약금.1]는 없는 파일도 있음'''
    print(main_path + file_)
    #op_instance = op.load_workbook(main_path + file_)
    df = pd.read_excel(main_path + file_, sheet_name="계약자")

    # 칼럼 이름 조정
    df = df.rename({"초기계약일":"계약일"}, axis=1)

    df = df[['단지명', '성명', '동', '호', '타입', '계약일', '변경보증금', '변경임대료', '변경잔금', '변경일']]
        
    if df_concat is not None:
        df_concat = pd.concat([df_concat, df], axis=0)
    else:
        df_concat = df
    #xlwb = xlApp.Workbooks.Open(main_path + file_, False, True, None, '2017')

df_concat = df_concat.reset_index()
breakpoint()
#df_concat.to_csv("정리.csv")

#pd.read_excel("")


def decryption(file_path):
    import msoffcrypto

    passwd = 'xyz'

    decrypted_workbook = io.BytesIO()
    with open(i, 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=passwd)
        office_file.decrypt(decrypted_workbook)