import logging


def scroll_to_next_screen():
    pass


def select_char():
    pass


def is_bottom_char_grid():
    return True


if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=20)

    while not is_bottom_char_grid():
        logging.debug("start looking char from screenshots")
        logging.debug("go to next screen")
