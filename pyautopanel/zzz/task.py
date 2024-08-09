import time

from loguru import logger

from pyautopanel.zzz.cnocr_ocr import CnOcrCtl


class Task:
    def __init__(self, _callback):
        self.ocrCtl = CnOcrCtl()
        self._round = 0
        self._running = False
        self._paused = False
        self._callback = _callback
        self.list = [
            '旧都列车',
            '旧都列车·前线',
            '下一步',
            '出战',
            '拒绝他的好意',
        ]
        self.next = 0

    def run(self):
        self._running = True
        self._paused = False
        while self._running:
            if self._paused:
                logger.debug('hollow search paused...')
                time.sleep(1)
                continue
            logger.debug('hollow search running...{}'.format(self._round))
            # do hollow search
            self._task()
            time.sleep(1)
            # self._round += 1
            # self._callback(self._round)

    def pause(self):
        self._paused = True

    def restart(self):
        self._paused = False

    def stop(self):
        self._running = False
        self._paused = False
        self._round = 0
        self.next = 0

    def _task(self):
        for current in range(self.next, len(self.list)):
            print('current:', current)
            if self.ocrCtl.click_target(self.list[current]):
                self.next = current + 1


if __name__ == '__main__':
    task = Task(lambda x: print(x))
    task.run()
