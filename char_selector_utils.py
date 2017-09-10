import logging

import cv2

from adb_wrapper import screencap
from char_selector import find_char_card


def scroll_to_next_screen():
    pass


def select_char():
    pass


def is_bottom_char_grid():
    return True


def get_screen()
    file = "char_screen.png"
    screencap(file)
    screen = cv2.imread("screencaps/%s" % file)
    return screen

if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=10)

    screen = get_screen()

    while not is_bottom_char_grid():
        logging.debug("start looking char from screenshots")
        pts = find_char_card(screen)

        logging.debug("go to next screen")
