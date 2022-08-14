import time


class timeU:
    def __init__(self, weight=1):
        self.weight = weight
        pass

    def sleep(self, mag):
        time.sleep(mag * self.weight)
