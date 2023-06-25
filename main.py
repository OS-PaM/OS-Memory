from page_schedule.tool.terminal_input import terminal_input as Terminal_input
from page_schedule.tool.random_input import random_input as Random_input
from page_schedule.core.controller import controller
from page_schedule.core.memory_frame import memory_frame


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

    info_input = by_user()
    ctrl = info_input[0]
    alg = info_input[1]
    print("按任意键确认执行")
    input()
    while True:
        try:
            print(ctrl(alg))
        except NameError as error:
            print(error)
            break
    print()
    ctrl.print_all()



