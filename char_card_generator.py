import logging


def is_bottom():
    return False


if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=10)

    """ this code assume you are at the char select screen
        we will keep finding char card until it scrolls till it reaches bottom
        for each char card it exports to test_input/char_cards
    """
    while not is_bottom():
        pass
