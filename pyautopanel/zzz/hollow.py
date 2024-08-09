import time

from loguru import logger


class Hollow:
    def __init__(self, _callback):
        self._round = 0
        self._running = False
        self._paused = False
        self._callback = _callback

    def run(self):
        self._running = True
        self._paused = False
        while self._running:
            if self._paused:
                logger.debug('timer paused...')
                time.sleep(1)
                continue
            self.second += 1
            logger.debug('timer running...{}'.format(self.second))
            self._callback(self.time)
            time.sleep(1)

    def pause(self):
        self._paused = True

    def restart(self):
        self._paused = False

    def stop(self):
        self._running = False
        self._paused = False
        self._round = 0
