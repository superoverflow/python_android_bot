import logging
import time

import cv2

import adb_wrapper


def battle_loop():
    logging.debug("click battle loop")
    repeat_btn = ("993", "660")
    cancel_btn = ("860", "192")
    adb_wrapper.click(repeat_btn)
    adb_wrapper.click(cancel_btn)
    adb_wrapper.screencap("battleloop.png")
    time.sleep(2)
    scrn = cv2.imread("screencaps/battleloop.png")
    h, w = scrn.shape[:2]
    scrn_resized = cv2.resize(scrn, (w / 5, h / 5), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("battleloop", scrn_resized)
    cv2.waitKey(1)


if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=10)
    adb_wrapper.connect("192.168.0.10", 5555)

    while 1:
        battle_loop()
