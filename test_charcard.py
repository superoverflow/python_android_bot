import unittest
from os import listdir, path

from charcard import CharCard

TEST_DATA_DIR = "test_input/char_cards/"


class CharCardTest(unittest.TestCase):
    def read_meta(self):
        metafile = path.join(TEST_DATA_DIR, "meta.txt")

        with open(metafile) as f:
            lines_with_header = f.readlines()
            lines = lines_with_header[1:]
            result = [tuple(l.strip('\s\n').split(",")) for l in lines]
            result = [(r[0], int(r[1]), int(r[2])) for r in result]
        return result

    def search_char_chars(self):
        return [f for f in listdir(TEST_DATA_DIR) if f.endswith('.png')]

    def test(self):
        cases = self.read_meta()

        for c in cases:
            file = path.join(TEST_DATA_DIR, c[0])
            char = CharCard(file)
            print("%s, %s, %s" % (c, char.is_four_stars(), char.is_lv_40()))


if __name__ == '__main__':
    unittest.main()
