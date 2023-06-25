import os
import random

from page_schedule.core.scheduler import scheduler
from page_schedule.core.scheduler.fifo import fifo as FIFO
from page_schedule.core.scheduler.lru import lru as LRU
from page_schedule.core.scheduler.opt import opt as OPT


class random_input:
    blocks: int
    pages: list[int]
    alg: scheduler
    alg_str: str
    clear_str = 'cls'

    def __init__(self):
        self.alg = FIFO()
        self.blocks = 0
        self.pages = []

    def input(self):
        alg = random.randrange(1, 4)
        if alg == 1:
            self.alg = FIFO()
            self.alg_str = "FIFO"
        elif alg == 2:
            self.alg = LRU()
            self.alg_str = "LRU"
        elif alg == 3:
            self.alg = OPT()
            self.alg_str = "OPT"
        self.blocks = random.randrange(3, 9)
        page_length = random.randrange(self.blocks, 17)
        while page_length:
            page_length = page_length - 1
            self.pages.append(random.randrange(1, min(20, 3*self.blocks)))

        os.system(self.clear_str)
        print("随机完成 随机的数据为: ")
        print("内存块数: " + str(self.blocks))
        print("页块列表: " + str(self.pages))
        print("所选算法: " + self.alg_str)

    def get_alg(self):
        return self.alg

    def get_blocks(self):
        return self.blocks

    def get_pages(self):
        return self.pages


