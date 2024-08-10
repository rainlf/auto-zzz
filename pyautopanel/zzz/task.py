import time

import yaml
from loguru import logger

import pyautopanel.zzz.task_executor as task_executor
from pyautopanel.zzz.constants import *


class Task:
    def __init__(self, fighter, _callback):
        self._running = False
        self._paused = False
        self._round = 0
        self._stage_idx = 0
        self._step_idx = 0
        self._fighter = fighter
        self._callback = _callback

    def _init(self):
        self._running = True
        self._paused = False
        self._round = 0
        self._stage_idx = 0
        self._step_idx = 0
        self._load_config()

    def run(self):
        self._init()
        logger.info('task running..., fighter: {}'.format(self._fighter))
        while self._running:
            if self._paused:
                logger.debug('hollow search paused...')
                time.sleep(1)
                continue
            logger.debug('hollow search running...{}'.format(self._round))
            # do hollow search
            self._task()
            time.sleep(1)

    def pause(self):
        self._paused = True

    def restart(self):
        self._paused = False

    def stop(self):
        self._running = False
        self._paused = False
        self._round = 0
        self._stage_idx = 0
        self._step_idx = 0

    def _load_config(self):
        with open(TASK_CONFIG, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            self._task_config = data['taskStages']
            self._task_stages = list(self._task_config.keys())

    def _task(self):
        # find current stage
        stage = self._task_stages[self._stage_idx]
        logger.info('current stage: {}'.format(stage))

        # find current step
        steps = self._task_config[stage]
        step = steps[self._step_idx]

        # do step
        if task_executor.do_step(step):
            # success do next step
            self._step_idx += 1
        else:
            # failed try continue
            task_executor.do_continue()

        # check stage done
        if self._step_idx >= len(steps):
            self._step_idx = 0
            self._stage_idx += 1
            logger.debug('current stage done: {}'.format(self._stage_idx))
            if self._stage_idx >= len(self._task_stages):
                self._stage_idx = 0
                self._round += 1
                logger.debug('all stages done: {}'.format(self._round))
                self._running = False


if __name__ == '__main__':
    task = Task('No.11', lambda x: print(x))
    task.run()
    pass
