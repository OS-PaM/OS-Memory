from page_schedule.core.memory_frame import memory_frame
from page_schedule.core.scheduler.scheduler import Scheduler


class fifo(Scheduler):

    def __init__(self):
        super().__init__()

    def __call__(self, memory: memory_frame,
                 ready_pages: list[int]):

        page = ready_pages[0]
        if memory.append(page):
            return True, True                   # 进行添加操作 添加成功 说明没有发生缺页/替换 命中
        else:
            if not memory.contains(page):       # 如果不存在而且放入失败 说明内存已满 发生了缺页/替换
                memory.pop_first()
                memory.append(page)
                return True, True
            else:
                return False, False             # 如果存在而且放入失败 说明内存未满 发生了缺页/替换 （替换空页）
