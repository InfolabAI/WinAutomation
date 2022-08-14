import time


class TimeU:
    def __init__(self, weight=1):
        self.weight = weight

    def sleep(self, mag):
        time.sleep(mag * self.weight)
