from functions_pyautogui_msgbox import Msgbox
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from functions_initialization import *
from functions_interface import InterfaceU
from functions_process import Manage_process
from functions_saving_a_paper import Manage_saving
from functions_print_files_in_a_folder import Print_files_in_a_folder


class Manage_selenium_IE(InterfaceU):
    def __init__(self, init):
        super().__init__()
        self.mp = Manage_process()
        self.msaving = Manage_saving()
        self.pff = Print_files_in_a_folder(password_list=init.password)
        self.skip_num = init.skip_num

    def wait_login(self):
        """
        IE를 실행하고, 사용자가 필요한 화면에 도달할 때까지 기다림"""
        # WebDriver를 이용해 IE을 실행
        driver = webdriver.Ie(".\\IEDriverServer.exe")
        gh_path = "http://g0.gh.or.kr"

        # 사이트로 이동
        driver.get(gh_path + "/jsp/Main.jsp")

        """
        Explorer 로그인, 문서함, 원하는 화면 띄우기를 기다리기
        """
        ret = Msgbox.confirm(
            text="현재 실행된 explorer 에서 로그인 후, 문서함에 출력할 게시글만 조건부 검색을 한 후 OK를 눌러주세요. \n\n문서함의 조건부 검색된 모든 문서 및 첨부파일을 자동으로 페이지를 넘겨가며 모두 인쇄합니다. \n\n조건의 예) 기간 조건, 제목 조건 등",
            title="안내 사항",
        )
        if ret:
            pass
        else:
            exit()

        self.driver = driver

    def move_to_target_frame(self):
        """
        목표 frame 으로 이동.
        
        HTML 상에는 게시글 관련 코드가 없고, frame 내부로 한단계씩 타고 들어가며 새로운 html 을 가져와야 함
        아래는 IE 전용 코드이고, chrome 은 다른 코드를 사용해야 함
        https://stackoverflow.com/questions/28761461/i-am-not-able-to-switch-to-iframe-using-internet-explorer
        """
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "Start"))
        self.driver.switch_to.frame(
            self.driver.find_element(By.NAME, "doc_frame_right")
        )

    def get_document_element_list(self):
        """
        문서함에서 각 게시글에 해당하는 element 의 list를 가져옴.

        IE 의 개발자모드에서 HTML source 를 보며 게시글에 해당하는 element 를 가져옴
        https://selenium-python.readthedocs.io/locating-elements.html
        """
        elements = self.driver.find_elements(
            By.XPATH,
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a[@class='Table']",
        )

        html_el_list = []
        # 현재 조건으로는 [제목, 수신자, 제목, 수신자, ...] 와 같이 선택됨. 그래서 0,2,4,6.. 으로 짝수만 선택하기 위해 [0::2] 사용.
        for html_el in elements[0::2]:
            html_el_list += [html_el]

        return html_el_list

    def get_page_element(self):
        """
        page 선택 버튼을 가져옴.
        현재 선택된 page 의 class 는 PageCrnt 이기 때문에, 아래만 반환됨. 여기서 ... 은 빼야함.
        (Pdb) p [el.text for el in elements]
        ['2', '3', '4', '5', '6', '7', '8', '9', '10', '...']
        """
        elements = self.driver.find_elements(
            By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr/td/a[@class='Page']",
        )
        cur_element = self.driver.find_elements(
            By.XPATH,
            "/html/body/table/tbody/tr/td/table/tbody/tr/td/a[@class='PageCrnt']",
        )
        cur_page = int(cur_element[0].text)

        html_pages_el_list = []
        for html_pages_el in elements:
            if "..." not in html_pages_el.text and int(html_pages_el.text) > cur_page:
                # ... 은 제외함. 또한 현재 보고 있는 페이지보다 뒷 페이지만 리턴함.
                html_pages_el_list += [html_pages_el]

        return html_pages_el_list

    def end_to_end(self):
        """
        login 부터 모든 게시글 저장까지를 담당하는 총괄 함수"""
        self.wait_login()
        self.move_to_target_frame()


        tmp_skip_num = 0 
        with open('./입력 상황.txt', 'w', encoding = 'cp949') as ftext:
            html_pages_el_list = self.get_page_element()
            while True:
                # 현재 페이지 처리
                html_el_list = self.get_document_element_list()
                for html_el in html_el_list:
                    tmp_skip_num += 1
                    if tmp_skip_num <= int(self.skip_num):
                        continue
                        
                    while True:
                        process_el = self.mp.retry_click_until_process_open(html_el)
                        #os.system(command_kill_format + exe_name_dict["groupware"])
                        self.msaving.saving_files_in_one_paper(process_el)
                        is_saved = self.pff.print_files_in_a_folder(tmp_path)
                        if is_saved:
                            break

                    ftext.write(html_el.text)

                if len(html_pages_el_list) == 0:
                    break

                # 다음 페이지 넘기기
                page_el = html_pages_el_list[0] # 보지 않은 페이지 중 첫 번재 페이지.
                try:
                    # 혹시나 첫번째 클릭으로 넘어가면 두 번재 클릭 때, 에러가 나기 때문.
                    page_el.click()
                    self.time.sleep(1)
                    page_el.click()
                    self.time.sleep(3)
                except:
                    pass
                html_pages_el_list = self.get_page_element()
            
            Msgbox.alert(text="종료되었습니다.", title="안내")
