import threading
import time

from loguru import logger


class Timer:
    def __init__(self):
        self._running = False
        self._paused = False
        self.second = 0

    def run(self):
        self._running = True
        self._paused = False
        while self._running:
            if self._paused:
                logger.info('timer paused...')
                time.sleep(1)
                continue
            self.second += 1
            logger.info('timer running...{}'.format(self.second))
            time.sleep(1)

    def pause(self):
        self._paused = True

    def restart(self):
        self._paused = False

    def stop(self):
        self._running = False
        self._paused = False
        self.second = 0

    @property
    def time(self):
        hours, remainder = divmod(self.second, 3600)
        minutes, seconds = divmod(remainder, 60)

        # 使用 f-string 格式化输出时间
        time_str = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds))
        return time_str


def main():
    timer = Timer()
    threading.Thread(target=lambda x: x.run(), args=(timer,)).start()
    logger.info('time: {}'.format(timer.time))
    time.sleep(3)
    
    timer.pause()
    logger.info('time: {}'.format(timer.time))
    time.sleep(3)

    timer.restart()
    logger.info('time: {}'.format(timer.time))
    time.sleep(3)

    logger.info('time: {}'.format(timer.time))
    timer.stop()
    logger.info('time: {}'.format(timer.time))


if __name__ == '__main__':
    main()
