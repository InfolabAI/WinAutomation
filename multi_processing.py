import os
import subprocess
import time
from functions_pyautogui_msgbox import Msgbox
from multiprocessing import Process


def terminate(name):
    ret = None
    while ret is None:
        ret = Msgbox.alert(text="프로그램을 종료하시겠습니까?", title="확인")
    # 화면 출력없이 실행
    os.popen("taskkill /f /pid " + str(os.getppid())).read()


if __name__ == "__main__":
    print("pid of main:", os.getpid())

    p1 = Process(target=terminate, args=("proc_1",))
    p1.start()
    # p1.join()

    while True:
        for i in range(10000):
            time.sleep(1)
            print(i)
