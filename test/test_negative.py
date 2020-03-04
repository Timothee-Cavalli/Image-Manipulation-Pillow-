#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image, ImageChops
import unittest
import sys
import os

sys.path.append("..\\src")

from negative import *

class Test(unittest.TestCase):

    def test_negative(self):


        img = Image.open("../image/spidey.jpg")
        img2 = Image.open("../image/spidey.jpg")

        negative(img2)

        size_x, size_y = img.size

        for y in range(size_y):
            for x in range(size_x):
                self.assertNotEqual(img.getpixel((x,y)), img2.getpixel((x,y)))


if __name__ == '__main__':
    unittest.main()
