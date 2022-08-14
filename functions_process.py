import pywinauto
from functions_interface import InterfaceU
from pywinauto.application import Application


class Manage_process(InterfaceU):
    def __init__(self):
        super().__init__()
        self.patience_num = 10
        pass

    @classmethod
    def find_element_with_name(self, name):
        """
        특정 name 을 가지는 process 의 element 를 가져옴.
        이 element 를 class name, handle, name 을 가지고 있음.
        """
        count = 0
        ret_el = None
        for el in pywinauto.findwindows.find_elements():
            if name in el.name:
                count += 1
                ret_el = el

        # if count >= 2:
        #    self.raise_error(text="동일한 이름을 포함한 process가 2개 이상입니다.")
        # else:
        #    return ret_el
        return ret_el

    def retry_click_until_process_open(self, html_el):
        """
        click 시, process가 켜지는 것이 확실하다는 가정하에, 켜질때까지 click함.
        """
        process_el = None
        for i in range(self.patience_num + 1):
            html_el.click()
            self.time.sleep(2)
            main_text = html_el.text.lstrip(" ").rstrip(" ").rstrip(".").rstrip(" ")
            process_el = self.find_element_with_name(main_text)
            if process_el is not None:
                break

        if i == self.patience_num:
            self.raise_error(
                str(self.patience_num) + "번 게시글을 클릭했지만, process가 실행되지 않았습니다."
            )

        return process_el

    def wait_for_process_open_with_name(self, name):
        """
        name 의 process 가 실행될때까지 확인하며 기다림
        """
        process_el = None
        for i in range(self.patience_num + 1):
            self.time.sleep(0.5)
            process_el = self.find_element_with_name(name)
            if process_el is not None:
                break

        if i == self.patience_num:
            self.raise_error(str(self.patience_num) + "번 기다렸지만, process가 실행되지 않았습니다.")

        return process_el

    def wait_once_for_process_open_with_name(self, name):
        """
        name 의 process 가 실행되었는지 확인하고, 실행되면 True 아니면 False
        """
        self.time.sleep(0.5)
        process_el = self.find_element_with_name(name)
        if process_el is None:
            return False
        else:
            return True

    def wait_for_process_kill_with_name(self, name):
        """
        name 의 process 가 꺼질때까지 확인하며 기다림
        """
        for i in range(self.patience_num + 1):
            if self.wait_once_for_process_kill_with_name(name):
                break

        if i == self.patience_num:
            self.raise_error(str(self.patience_num) + "번 기다렸지만, process가 종료되지 않았습니다.")

    def wait_once_for_process_kill_with_name(self, name):
        """
        name 의 process 가 종료되었는지 확인하고, 종료되면 True 아니면 False
        """
        self.time.sleep(0.5)
        process_el = self.find_element_with_name(name)
        if process_el is not None:
            print(process_el.name)
            return False
        else:
            return True

    def open_window_with_handle(self, handle):
        # found_index 0는 pywinauto.findwindows.ElementAmbiguousError 를 없애기 위해 사용.
        return Application().connect(handle=handle).window(found_index=0)

    def open_window_with_name(self, name):
        # found_index 0는 pywinauto.findwindows.ElementAmbiguousError 를 없애기 위해 사용.
        return pywinauto.Application().connect(title=name).window(found_index=0)

    def open_window_with_class_name(self, class_name):
        # found_index 0는 pywinauto.findwindows.ElementAmbiguousError 를 없애기 위해 사용.
        return (
            pywinauto.Application().connect(class_name=class_name).window(found_index=0)
        )

    def wait_with_class_name(self, try_num, interval, class_name):
        for i in range(try_num):
            self.time.sleep(interval)
            list_ = pywinauto.findwindows.find_elements(class_name=class_name)
            if len(list_) != 0:
                return True

        return False

    def wait_with_name(self, try_num, interval, name):
        for i in range(try_num):
            self.time.sleep(interval)
            list_ = pywinauto.findwindows.find_elements(title=name)
            if len(list_) != 0:
                return True

        return False
