import os

import cv2

test_input_dir = 'test_input/char_cards/'
test_files = [f for f in os.listdir(test_input_dir) if f.endswith(".png")]

# test_files = [ '02282_000.png', '02282_001.png', '02282_002.png']
base = (82, 42)
size = (24, 30)

for file in test_files:
    raw = cv2.imread(test_input_dir + file)
    img = raw[base[0]:base[0] + size[0], base[1]:base[1] + size[1]]
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

    cv2.imshow('sample', img)
    cv2.waitKey()
