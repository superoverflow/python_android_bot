import logging
import os
import sys

import cv2
import numpy as np

test_input_dir = 'test_input/char_cards/'
test_files = [f for f in os.listdir(test_input_dir) if f.endswith(".png")]

# test_files = [ '02282_000.png', '02282_001.png', '02282_002.png']
base = (82, 42)
size = (24, 30)


def cnt_height(cnt):
    [x, y, w, h] = cv2.boundingRect(cnt)
    return h


def keys_to_num(keys):
    """ given [1,4,7] output 147"""
    logging.debug(keys)
    return sum([n * 10 ** (i) for (i, n) in enumerate(keys[::-1])])


def capture_keys(keys):
    key = cv2.waitKey()

    logging.debug(keys)

    if key == 27:  # ESC
        sys.exit()
    elif key == 13:  # Enter
        logging.debug(keys)
        return keys
    elif key in range(48, 58):  # 0-9
        key = key - ord("0")
        keys.append(key)
        logging.debug(keys)
        return capture_keys(keys)
    else:
        logging.debug("unexpected key pressed")

for file in test_files:
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=10)

    raw = cv2.imread(test_input_dir + file)
    img = raw[base[0]:base[0] + size[0], base[1]:base[1] + size[1]]
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # we want to have contour large and taill enough
    contours_filtered = [cnt for cnt in contours
                         if cv2.contourArea(cnt) > 15 and
                         cnt_height(cnt) > 14]

    mask = np.zeros(size, np.uint8)
    cv2.drawContours(mask, contours_filtered, -1, (255, 255, 255), 1)

    cv2.imshow(file, mask)
    keys_captured = capture_keys([])
    lv = keys_to_num(keys_captured)
    print(file, lv)
