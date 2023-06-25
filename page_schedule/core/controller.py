from copy import deepcopy

from page_schedule.core.memory_frame import memory_frame
from page_schedule.core.scheduler import scheduler


class controller:
    memory: memory_frame

    fault_times: int = 0
    replace_times: int = 0
    len = 0
    pages: [int]
    state: bool = False

    def __init__(self, memory: memory_frame, pages: list[int]):
        self.memory = memory
        self.pages = deepcopy(pages)
        self.len = len(pages)
        pass

    def __call__(self, alg: scheduler):
        if len(self.pages) != 0:
            self.state = True
            return_state = alg(self.memory, self.pages)
            if return_state[0]:
                self.fault_times = self.fault_times + 1
            if return_state[1]:
                self.replace_times = self.replace_times + 1
            self.pages.pop(0)
            self.state = False
            return str(self.memory)
        if not self.state:
            raise NameError("所有的请求的Pages均已在内存中完成命中/替换")
        pass

    def print_all(self):
        self.print_fault_times()
        self.print_replace_times()
        self.print_fault_odds()

    def print_fault_times(self):
        print("缺页次数: " + str(self.fault_times))

    def print_replace_times(self):
        print("替换次数: " + str(self.replace_times))

    def print_fault_odds(self):
        print("缺页概率: " + str(self.fault_times / self.len))
