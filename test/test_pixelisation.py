#! /usr/bin/env python3
#-*- conding utf-8 -*-

import unittest
import sys
import os

sys.path.append("..\\src")

from pixelisation import *


class TestPixelisation(unittest.TestCase):

    def test_pixelisation(self):
        img = Image.open("../image/spidey.jpg")

        size_x, size_y = img.size

        #just 2 big pixel so the test code is simpler to read and understand
        pixelisation(img, 500)


        for x in range(size_x):
            for y in range(500):
                self.assertEqual(img.getpixel((0,0)), img.getpixel((x,y)))
            for y in range(500, size_y):
                self.assertEqual(img.getpixel((0,500)), img.getpixel((x,y)))




if __name__ == '__main__':
    unittest.main()
