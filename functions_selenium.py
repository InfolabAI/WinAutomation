from functions_pyautogui_msgbox import Msgbox
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from functions_interface import InterfaceU
from functions_process import Manage_process
from functions_saving_a_paper import Manage_saving


class Manage_selenium_IE(InterfaceU):
    def __init__(self):
        super().__init__()
        self.mp = Manage_process()
        self.msaving = Manage_saving()

    def wait_login(self):
        """
        IE를 실행하고, 사용자가 필요한 화면에 도달할 때까지 기다림"""
        # WebDriver를 이용해 IE을 실행
        driver = webdriver.Ie(
            "C:\\Users\\AdmiN\\automation\\driver\\ie\\IEDriverServer.exe"
        )
        gh_path = "http://g0.gh.or.kr"

        # 사이트로 이동
        driver.get(gh_path + "/jsp/Main.jsp")

        """
        Explorer 로그인, 문서함, 원하는 화면 띄우기를 기다리기
        """
        ret = Msgbox.confirm(
            text="현재 실행된 explorer 에서 로그인 후, 문서함에 출력할 게시글만 조건부 검색을 해주세요. 문서함의 조건부 검색된 모든 문서 및 첨부파일을 자동으로 페이지를 넘겨가며 모두 인쇄합니다. 문서함에 조건부 검색을 완료했다면 확인을 눌러주시고, 종료하려면 취소를 눌러주세요.\n조건의 예) 기간 조건, 제목 조건 등",
            title="안내 사항",
        )
        if ret == "취소":
            exit()

        self.driver = driver

    def get_document_element_list(self):
        """
        문서함에서 각 게시글에 해당하는 element 의 list를 가져옴.

        HTML 상에는 게시글 관련 코드가 없고, frame 내부로 한단계씩 타고 들어가며 새로운 html 을 가져와야 함
        아래는 IE 전용 코드이고, chrome 은 다른 코드를 사용해야 함
        https://stackoverflow.com/questions/28761461/i-am-not-able-to-switch-to-iframe-using-internet-explorer
        """
        from selenium.webdriver.common.by import By

        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "Start"))
        self.driver.switch_to.frame(
            self.driver.find_element(By.NAME, "doc_frame_right")
        )

        """
        IE 의 개발자모드에서 HTML source 를 보며 게시글에 해당하는 element 를 가져옴
        https://selenium-python.readthedocs.io/locating-elements.html
        """
        elements = self.driver.find_elements(
            By.XPATH,
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[@class='Bsc']",
        )

        ret_el_list = []
        # 위 코드는 완벽하진 않지만, 예외적인 Bsc 를 모두 클릭해도 문제는 없음.
        for html_el in elements:
            if html_el.size["width"] > 250:
                # size로 구분
                ret_el_list += [html_el]

        return ret_el_list

    def end_to_end(self):
        """
        login 부터 모든 게시글 저장까지를 담당하는 총괄 함수"""
        self.wait_login()

        # TODO 페이지를 넘기는  for문이 하나 더 들어가야 함
        html_el_list = self.get_document_element_list()

        for html_el in html_el_list:
            process_el = self.mp.retry_click_until_process_open(html_el)
            self.msaving.saving_files_in_one_paper(process_el)

