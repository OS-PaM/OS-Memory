from page_schedule.core.memory_frame import memory_frame
from page_schedule.core.scheduler.scheduler import Scheduler


class opt(Scheduler):

    def __init__(self):
        super().__init__()

    def __call__(self, memory: memory_frame,
                 ready_pages: list[int]):

        page = ready_pages[0]
        if memory.append(page):
            return True, True  # 进行添加操作 添加成功 说明没有发生缺页/替换 命中
        else:
            if not memory.contains(page):  # 如果不存在而且放入失败 说明内存已满 发生了缺页/替换

                # 页面替换操作 待完善
                memory_pages = memory.get_all()

                fin_latest_value = 0  # 用于记录内存中最晚使用页号在队列中的索引
                fin_latest_index = 0  # 用于记录内存中最晚使用页号在内存中的索引

                for memory_index, memory_page in enumerate(memory_pages):
                    latest_value: int = -1
                    for ready_index, ready_page in enumerate(ready_pages):
                        if memory_page[0] == ready_page and latest_value < ready_index:
                            latest_value = ready_index
                    if latest_value == -1:  # 如果是 -1 代表就绪队列里不存在该值 以后不会使用 直接break
                        fin_latest_index = memory_index
                        break
                    elif latest_value > fin_latest_value:  # 找到了更晚使用的页号
                        fin_latest_value = latest_value
                        fin_latest_index = memory_index

                memory.pop(fin_latest_index)
                memory.append(page)
                return True, True
            else:
                return False, False  # 如果存在而且放入失败 说明内存未满 发生了缺页/替换 （替换空页）
