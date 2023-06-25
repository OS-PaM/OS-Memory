from abc import ABC, abstractmethod

from page_schedule.core.memory_frame import memory_frame


class Scheduler(ABC):

    @abstractmethod
    def __call__(self, memory: memory_frame,
                 ready_pages: list[int]) -> int:
        """
        :param memory: 模拟内存
        :param ready_pages: 就绪的页列表
        :return bool,bool: 结束算法,返回两个布尔值  No1.存在缺页返回True  No2.存在替换返回True
        """
        pass
