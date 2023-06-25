from page_schedule.core.controller import controller
from page_schedule.core.memory_frame import memory_frame
from page_schedule.tool.random_input import random_input as Random_input
from page_schedule.tool.terminal_input import terminal_input as Terminal_input


def by_user():
    terminal_input = Terminal_input()
    terminal_input.input()
    t_alg = terminal_input.get_alg()
    memory = memory_frame(terminal_input.get_blocks())
    t_ctrl = controller(memory, terminal_input.pages)
    return t_ctrl, t_alg


def by_random():
    random_input = Random_input()
    random_input.input()
    r_alg = random_input.get_alg()
    memory = memory_frame(random_input.get_blocks())
    r_ctrl = controller(memory, random_input.pages)
    return r_ctrl, r_alg


if __name__ == '__main__':

    info_input = None

    while True:
        try:
            print("1. 用户输入 | 2. 随机生成")
            choice = int(input("请输入数据来源模式: "))
            if choice == 1:
                info_input = by_user()
            elif choice == 2:
                info_input = by_random()
            else:
                raise ValueError
        except ValueError:
            print("类型错误 请重新输入")
            continue
        print("无输入回车后确认执行 或 输入任意内容回车后重新输入")
        enter = input()
        if enter == "":
            break
        else:
            continue
    ctrl = info_input[0]
    alg = info_input[1]

    while True:
        try:
            print(ctrl(alg))
        except NameError as error:
            print(error)
            break
    print()
    ctrl.print_all()
