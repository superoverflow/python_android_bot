import logging
import unittest
from os import path

from charcard import CharCard

TEST_DATA_DIR = "test_input/char_cards/"

"""This test script generates test cases from meta.txt

"""

def read_meta():
    metafile = path.join(TEST_DATA_DIR, "meta.txt")

    with open(metafile) as f:
        lines_with_header = f.readlines()
        lines = lines_with_header[1:]
        result = [tuple(l.strip('\s\n').split(",")) for l in lines]
        result = [(r[0], int(r[1]), int(r[2])) for r in result]
    return result


def make_test_func(desc, a, b):
    def test(self):
        self.assertEqual(a, b, desc)

    return test


class CharCardTest(unittest.TestCase):
    longMessage = True

if __name__ == '__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=20)

    meta = read_meta()

    char_cards = {c[0]: CharCard(TEST_DATA_DIR + c[0]) for c in meta}
    char_stars = {c[0]: c[1] for c in meta}
    char_lv = {c[0]: c[2] for c in meta}

    for k, v in char_cards.iteritems():
        test_func_star = make_test_func(k, char_stars[k] == 4, v.is_four_stars())
        test_func_lv = make_test_func(k, char_lv[k] == 40, v.is_lv_40())
        test_name = k.strip('.png')
        setattr(CharCardTest, 'test_{0}_stars'.format(test_name), test_func_star)
        setattr(CharCardTest, 'test_{0}_lv'.format(test_name), test_func_lv)

    unittest.main()
