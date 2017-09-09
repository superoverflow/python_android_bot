import cv2
import numpy as np
import logging

def find_pic(large, small, threshold):
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(large, small, method)
    loc = np.where(res >= threshold)
    cord = zip(*loc[::-1])
    cord = sorted(cord, key = lambda x: x[0]*x[0] + x[1]*x[1] )
    uniq_cord = uniq(cord)

    logging.debug("find %d object from screen" % len(uniq_cord))
    return uniq_cord

def uniq(a):
    return [ a[i] for i in range(len(a))
             if i==0 or not is_near(a[i], a[i-1]) ]

def is_near(a, b, threshold=3):
    """ check if a point is  near another one"""
    if (abs(a[0] - b[0]) <= threshold and
       abs(a[1] - b[1]) <= threshold):
       return True
    else:
       return False

def mark_pic(large, pt, size):
    """ in a larger pic, mark a rect from pt"""
    w, h = size[0], size[1]
    color = (0, 0, 255)
    thickness = 1
    cv2.rectangle(large, pt, (pt[0] + w, pt[1] + h), color, thickness)
