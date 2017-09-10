import logging

import cv2

from adb_wrapper import screencap, swipe
from char_selector import GRID_TOP_LEFT
from char_selector import find_char_card

def scroll_to_next_screen():
    pass


def select_char():
    pass


def is_bottom_char_grid():
    return True


def get_screen():
    file = "char_screen.png"
    screencap(file)
    screen = cv2.imread("screencaps/%s" % file)
    return screen

if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=10)

    screen = get_screen()

    logging.debug("start looking char from screenshots")
    pts = find_char_card(screen)
    ref = pts[-1]

    logging.debug("go to next screen")
    swipe(ref, GRID_TOP_LEFT)
