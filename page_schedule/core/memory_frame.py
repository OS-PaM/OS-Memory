class memory_frame:
    memory_block: list[list[int]]
    block: int

    def __init__(self, block):
        self.memory_block = []
        self.block = block

    def __str__(self):
        if len(self.memory_block) == 0:
            return "当前内存页面为空"
        else:
            strs = "当前内存页面列表: "
            out_page_list = []
            for page in self.memory_block:
                out_page_list.append(page[0])
            return strs + str(out_page_list)

    def append(self, page: int):
        if len(self.memory_block) == self.block:
            return False
        elif self.contains(page):
            self.add_used_times(page)
            return False
        else:
            self.memory_block.append([page, 0])
            return True

    def get_all(self):
        return self.memory_block

    def del_all(self):
        self.__init__(self.block)

    def contains(self, check_page: int):
        for index, page in enumerate(self.memory_block):
            if check_page == page[0]:
                return True
        return False

    def add_used_times(self, insert_page: int):
        for index, page in enumerate(self.memory_block):
            if insert_page == page[0]:
                page[1] = page[1] + 1
                return True
        return False

    def pop(self, index):
        self.memory_block.pop(index)

    def pop_first(self):
        if len(self.memory_block) == 0:
            raise OverflowError("Analog: There is no block to pop")
        else:
            self.memory_block.pop(0)

    def pop_end(self):
        if len(self.memory_block) == 0:
            raise OverflowError("Analog: There is no block to pop")
        else:
            self.memory_block.pop()
