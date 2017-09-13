from utils import *

""" just a quick try on opencv"""

GRID_TOP_LEFT = (837, 57)
GRID_BOTTOM_RIGHT = (1257, 545)
REF_ADJ = (-15, -86)
CARD_SIZE = (138, 123)
TMPL_LV='templates/lv.png'
TMPL_LV_40='templates/Lv40.png'
TMPL_FOUR_STARS='templates/four_stars.png'


def find_char_card(screen):
    """ for each ref pts, go to char card top left
        filter if the char grid hides the edges
    """
    tmpl_lv = cv2.imread(TMPL_LV)
    ref_pts = find_pic(screen, tmpl_lv, 0.69)
    card_refs = [_lv_to_card_ref(p) for p in ref_pts
                 if card_within_grid(p)]

    logging.debug("find %d object from screen" % len(card_refs))
    return card_refs


def _lv_to_card_ref(p):
    return tuple(np.add(p, REF_ADJ))


def card_within_grid(p):
    card_top = p[1] + REF_ADJ[1]
    card_bottom = p[1] + REF_ADJ[1] + CARD_SIZE[1]

    if (card_top > GRID_TOP_LEFT[1] and
        card_bottom < GRID_BOTTOM_RIGHT[1]):
        return True
    else:
        return False


def show_card(screen, pt):
    char_card = get_char_card(screen, pt)
    cv2.imshow("char", char_card)
    cv2.waitKey()


def get_char_card(screen, pt):
    char_card = screen[pt[1]:pt[1] + CARD_SIZE[1],
                pt[0]:pt[0] + CARD_SIZE[0]]
    return char_card


def is_found(pts):
    if len(pts)>0:
        return True
    else:
        return False


def is_char_lv_40(char):
    tmpl = cv2.imread(TMPL_LV_40)
    pts = find_pic(char,tmpl, 0.63)

    return is_found(pts)


def is_char_four_stars(char):
    tmpl = cv2.imread(TMPL_FOUR_STARS)
    pts = find_pic(char, tmpl, 0.91)

    return is_found(pts)


def char_need_train(char):
    is_four_stars = is_char_four_stars(char)
    is_lv_40 = is_char_lv_40(char)
    needs_training = is_four_stars and not is_lv_40
    logging.info("Char need training? 4 stars:[%5s] Lv 40:[%5s] => [%5s] ",
                 is_four_stars, is_lv_40, needs_training)

    return needs_training


def char_pos(ref_pt):
    return (ref_pt[0] + CARD_SIZE[0]/2,
            ref_pt[1] + CARD_SIZE[1]/2)


def mark_char_grid(screen):
    cv2.rectangle(screen, GRID_TOP_LEFT, GRID_BOTTOM_RIGHT, (0, 255, 255), 1)


def show_result(screen):
    cv2.imshow("result", screen)
    cv2.waitKey()


def find_char_needs_training(screen):

    result = []
    card_refs = find_char_card(screen)

    for pt in card_refs:
        char = get_char_card(screen, pt)
        if char_need_train(char):
            result.append(pt)


    return [ (r[0] + CARD_SIZE[0]/2 , r[1] + CARD_SIZE[1]/2) for r in result]


def gen_test_input(screen):
    import random

    random_key =random.randint(1,10000)
    card_refs = find_char_card(screen)

    for (cnt, pt) in enumerate(card_refs):
        cv2.imwrite("test_input/char_cards/%05d_%03d.png" % (random_key, cnt),
                    get_char_card(screen, pt))


if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=20)

    """
    img = [ 'char_card_07682_002.png',
            'char_card_06762_003.png',
            'char_card_05237_005.png'
            ]

    for i in img:
        card = cv2.imread('test_input/char_cards/%s' % i)

        logging.info(is_char_four_stars(card))
        logging.info(is_char_lv_40(card))
    """

    scrn = ['170913_195341.png',
            '170913_195359.png',
            '170913_195408.png',
            '170913_195416.png',
            '170913_195424.png',
            '170913_195431.png',
            '170913_195438.png',
            '170913_195445.png',
            '170913_195452.png',
            '170913_195459.png',
            '170913_195506.png',
            '170913_195513.png',
            '170913_195519.png',
            '170913_195526.png',
            '170913_195533.png',
            '170913_195540.png',
            '170913_195546.png',
            '170913_195554.png',
            '170913_195617.png']

    for i in scrn:
        logging.info("----- %s -------" % i)
        screen = cv2.imread('test_input/char_select_screens/%s' % i)
        #gen_test_input(screen)

        pts = find_char_needs_training(screen)
        [mark_pic(screen, pt, (20,20)) for pt in pts]

        cv2.imwrite("test_output/%s" % i , screen)


    #show_result(screen)

    # mark char grid
    #mark_char_grid(screen)

    # mark char cards
    #cv2.imwrite("result.png", screen)

