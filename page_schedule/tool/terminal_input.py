import os
import sys

from page_schedule.core.scheduler import scheduler
from page_schedule.core.scheduler.fifo import fifo as FIFO
from page_schedule.core.scheduler.lru import lru as LRU
from page_schedule.core.scheduler.opt import opt as OPT


class terminal_input:
    blocks: int
    pages: list[int]
    alg: scheduler
    alg_str: str
    clear_str: str

    def __init__(self):
        self.alg = FIFO()
        self.blocks = 0
        self.pages = []
        if sys.platform.startswith('win32'):
            self.clear_str = 'cls'
        else:
            self.clear_str = 'clear'

    def input(self):
        os.system(self.clear_str)
        while True:
            try:
                self.blocks = int(input("请输入内存块数: "))
                break
            except ValueError:
                print("类型错误 请重新输入")
                continue

        while True:
            try:
                self.pages = []
                page_list = input("请输入页块列表 以空字符串' '分割: ").split(" ")
                for page in page_list:
                    self.pages.append(int(page))
                break
            except ValueError:
                print("类型错误 请重新输入")
                continue

        while True:
            try:
                print("1. FIFO | 2. LRU | 3. OPT")
                alg = int(input("请输入编号: "))
                if alg == 1:
                    self.alg = FIFO()
                    self.alg_str = "FIFO"
                elif alg == 2:
                    self.alg = LRU()
                    self.alg_str = "LRU"
                elif alg == 3:
                    self.alg = OPT()
                    self.alg_str = "OPT"
                else:
                    raise ValueError
                break
            except ValueError:
                os.system(self.clear_str)
                print("不在范围内 请重新输入")
                continue

        os.system(self.clear_str)
        print("输入完成 输入的数据为: ")
        print("内存块数: " + str(self.blocks))
        print("页块列表: " + str(self.pages))
        print("所选算法: " + self.alg_str)

    def get_alg(self):
        return self.alg

    def get_blocks(self):
        return self.blocks

    def get_pages(self):
        return self.pages
