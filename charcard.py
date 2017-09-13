import cv2

from utils import is_found, find_pic

TMPL_LV = cv2.imread('templates/lv.png')
TMPL_LV_40 = cv2.imread('templates/Lv40.png')
TMPL_FOUR_STARS = cv2.imread('templates/four_stars.png')


class CharCard():
    """ This class represents a char card from char selection screen"""

    def __init__(self, img, coord):
        self.img = img
        self.coord = coord

    def __init__(self, file):
        self.img = cv2.imread(file)
        self.coord = (0, 0)

    def is_lv_40(self):
        pts = find_pic(self.img, TMPL_LV_40, 0.63)
        return is_found(pts)

    def is_four_stars(self):
        pts = find_pic(self.img, TMPL_FOUR_STARS, 0.91)
        return is_found(pts)
