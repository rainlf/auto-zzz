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
                logger.debug('hollow search paused...')
                time.sleep(1)
                continue
            self.second += 1
            logger.debug('hollow search running...{}')
            self._callback(self._round)

    def pause(self):
        self._paused = True

    def restart(self):
        self._paused = False

    def stop(self):
        self._running = False
        self._paused = False
        self._round = 0
