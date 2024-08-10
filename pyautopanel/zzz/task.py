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
        task_executor.fighter = self._fighter
        logger.info('task running..., fighter: {}'.format(self._fighter))
        while self._running:
            if self._paused:
                logger.debug('hollow search paused...')
                time.sleep(1)
                continue
            # logger.debug('hollow search running...{}'.format(self._round))
            # do hollow search
            self._task()
            # time.sleep(1)

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

        # find current step
        steps = self._task_config[stage]
        step = steps[self._step_idx]

        # do step
        success, next_stage = task_executor.do_step(step)
        if success:
            # success do next step
            self._step_idx += 1

        # check stage done
        if self._step_idx >= len(steps):
            self._step_idx = 0
            if next_stage:
                if next_stage == 'floor1.1':
                    self._task_stages.remove('floor1.2')
                else:
                    self._task_stages.remove('floor1.1')

                self._stage_idx = self._task_stages.index(next_stage)
            else:
                self._stage_idx += 1
            if self._stage_idx >= len(self._task_stages):
                self._stage_idx = 0
                self._round += 1
                logger.debug('all stages done: {}'.format(self._round))
                self._running = False


if __name__ == '__main__':
    task = Task('No.11', lambda x: print(x))
    task.run()
    pass
