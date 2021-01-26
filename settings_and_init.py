import pyautogui as pa
import random
import time


pa.FAILSAFE = True
PAUSE_BEFORE_ACTIONS = 3
CLICK = pa.click
SCROLL = pa.scroll
WIDTH, HEIGHT = pa.size()
TRIBUTE_ACTION = []
EXIT_ACTION = []


PATH = r"C:\Users\program\PycharmProjects\GUITest\buttons\ "


class Action():
    def __init__(self, command, target=None):
        self.command = command
        self.target = target

    def do_action(self):
        time.sleep(random.randrange(1, PAUSE_BEFORE_ACTIONS+1))
        print(self.target)
        if self.command == SCROLL:
            SCROLL(random.randrange(-60, 60))
        elif self.command == CLICK:
            if self.target == 'troop':
                CLICK(WIDTH/2, HEIGHT/2)
            elif self.target == 'top_right_bottom':
                CLICK(WIDTH, 10)
            else:
                try:
                    coords = find_on_screen(self.target)
                    if coords is None:
                        print('Координаты картинки ' + self.target + ' не найдены!')
                        return
                except pa.ImageNotFoundException:
                    print('Координаты картинки ' + self.target + ' не найдены!')
                    return
                width_to_click, height_to_click = pa.center(coords)
                # CLICK(moveto(width_to_click, height_to_click))
                CLICK(pa.moveTo(width_to_click, height_to_click, duration=0.25, tween=pa.easeOutQuad))


def actions_describe():
    troops_actions = [Action(CLICK, PATH.strip() + 'troops.png'), Action(SCROLL), Action(SCROLL), Action(CLICK, 'troop'),
                     Action(CLICK, PATH.strip() + 'troops_upgrade.png'), Action(CLICK, PATH.strip() + 'back_for_all.png'),
                     Action(CLICK, 'top_right_bottom'), Action(CLICK, PATH.strip() + 'collection.png'),
                     Action(CLICK, PATH.strip() + 'close_for_all.png'), Action(CLICK, PATH.strip() + 'back_for_all.png')]
    chest_actions = [Action(CLICK, PATH.strip() + 'chests.png'), Action(CLICK, PATH.strip() + 'close_for_all.png')]
    errand_board_actions = [Action(CLICK, PATH.strip() + 'errand_board.png')]
    actions_list = [chest_actions, troops_actions, errand_board_actions]

    TRIBUTE_ACTION = [Action(CLICK, PATH.strip() + 'tribute.png'), Action(CLICK, PATH.strip() + 'tribute_pass.png')]
    EXIT_ACTION = [Action(CLICK, PATH.strip() + 'exit.png'), Action(CLICK, PATH.strip() + 'exit_confirm.png')]

    return_list = actions_list[0:random.randrange(1, len(actions_list))]
    return_list.insert(0, TRIBUTE_ACTION)
    return_list.append(EXIT_ACTION)

    return return_list


def moveto(target_width, target_height):
    current_width, current_height = pa.position()
    while (current_width != target_width) or (current_height != target_height):
        current_width, current_height = pa.position()
        delta_width = current_width - target_width
        delta_height = current_height - target_height
        if delta_width < 0:
            shift_width = -1
        else:
            shift_width = 1
        if delta_height < 0:
            shift_height = -1
        else:
            shift_height = 1

        if abs(delta_width) < 50 and abs(delta_height) < 50:

            pa.moveTo(target_width, target_height, duration=0.5, tween=pa.easeInElastic)
            current_width = target_width
            current_height = target_height
            break

        pa.moveTo(current_width-(shift_width * random.randrange(1, 10)*abs(delta_width/100)), current_height-(shift_height * random.randrange(1, 10)*abs(delta_height/100)), duration=0.1, tween=pa.easeOutQuad)
    return current_width, current_height


def find_on_screen(path):
    return pa.locateOnScreen(path)


def check_events():
    pass
