import time


class TimeU:
    def __init__(self, weight=1):
        self.weight = weight

    def sleep(self, mag):
        print(f'{mag * self.weight} 초간 기다리는 중')
        time.sleep(mag * self.weight)
