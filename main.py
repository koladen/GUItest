import time
import settings_and_init as si


def do_all_actions(doing_actions):
    for action_list in doing_actions:
        for action in action_list:
            action.do_action()


def start():
    time.sleep(si.PAUSE_BEFORE_ACTIONS)
    list_of_actions = si.actions_describe()

    si.check_events()
    do_all_actions(list_of_actions)

    # width, height = pa.size()
    #
    # coords = find_on_screen(PATH.strip() + 'tribute.png')
    # width_to_click, height_to_click = pa.center(coords)
    # # pa.alert('Будем двигать?') # ВЫДАЕТ ОКНО С ВОПРОСОМ НА ЭКРАНЕ, ПОКА НЕ НАЖМЕШЬ ОК, НЕ БУДЕТ РАБОТАТЬ ДАЛЬШЕ
    # pa.doubleClick(moveto(width_to_click, height_to_click))
    # pa.doubleClick(r'C:\Users\program\PycharmProjects\GUITest\test.png') # НАХОДИТ КАРТИНКУ И КЛИКАЕТ
    # pa.moveTo(coords, duration=2, tween=pa.easeInOutQuad) # ВРОДЕ ПЛАВНО ДВИГАЕТСЯ К ЦЕЛИ
    # button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9) ИЩЕМ КАРТИНКУ ПОХОЖУЮ НА СКРИНШОТ, С ВЕРОЯТНОСТЬЮ 0.9. НАВЕРНОЕ ПОМОГЛО БЫ С КАЛЬКУЛЯТОРОМ
    # pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400)) ИЩЕМ КАРТИНКУ В ЗАДАННОЙ ОБЛАСТИ. ЗНАЧИТЕЛЬНО УСКОРЯЕТ ПОИСК
    # button7location = pyautogui.locateOnScreen('calc7key.png', grayscale=True) ИЩЕМ КАРТИНКУ В ОТТЕНКАХ СЕРОГО. НА 30% УСКОРЯЕТ ПОИСК


if __name__ == '__main__':
    start()


