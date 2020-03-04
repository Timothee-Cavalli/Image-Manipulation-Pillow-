#! /usr/bin/env python3
#-*- conding utf-8 -*-

import unittest
import sys
import os

sys.path.append("..\\src")

from thresholding import *

class Test(unittest.TestCase):


    def test_thresholding(self):

        img = Image.open("../image/spidey.jpg")
        img2 = Image.open("../image/spidey.jpg")
        img3 = Image.open("../image/spidey.jpg")
        img4 = Image.open("../image/spidey.jpg")

        binary = ((255, 255, 255), (0,0,0))
        # if this word exist
        fivenary = ((255, 255, 255), (0,0,0), (255,0,0), (0,255,0), (0,0,255))

        thresholding(img, 123, "R")
        thresholding(img2, 123, "G")
        thresholding(img3, 123, "B")
        thresholding(img4, 123)

        size_x,size_y = img.size
        for y in range(size_y):
            for x in range(size_x):
                self.assertIn(img.getpixel((x,y)), binary)
                self.assertIn(img2.getpixel((x,y)), binary)
                self.assertIn(img3.getpixel((x,y)), binary)
                self.assertIn(img3.getpixel((x,y)), fivenary)


if __name__ == '__main__':
    unittest.main()
