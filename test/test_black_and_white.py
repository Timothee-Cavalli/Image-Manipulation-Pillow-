#! /usr/bin/env python3
#-*- conding utf-8 -*-

import unittest
import sys
import os

sys.path.append("..\\src")

from black_and_white import *

class TestBlackAndWhite(unittest.TestCase):

    def test_black_and_white(self):
        img = Image.open("../image/spidey.jpg")

        black_and_white(img)

        size_x, size_y = img.size

        for y in range(size_y):
            for x in range(size_x):
                ppx = img.getpixel((x,y))
                self.assertEqual(ppx[0],ppx[1])
                self.assertEqual(ppx[0],ppx[2])
                self.assertEqual(ppx[1],ppx[2])



if __name__ == '__main__':
    unittest.main()
