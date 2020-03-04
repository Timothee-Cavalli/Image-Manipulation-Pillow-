#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image, ImageChops
import unittest
import sys
import os

sys.path.append("..\\src")

from shuffling import *

class TestShuffling(unittest.TestCase):

    def test_shuffling(self):
        img = Image.open("../image/spidey.jpg")
        img2 = Image.open("../image/spidey.jpg")
        img3 = Image.open("../image/spidey.jpg")

        size_x, size_y = img.size

        shuffling(img2, 10)
        shuffling(img3, 10)

        res =  ImageChops.difference(img, img2).getbbox() #return None if no difference
        self.assertIsNotNone(res)

        res =  ImageChops.difference(img, img3).getbbox() #return None if no difference
        self.assertIsNotNone(res)

        res =  ImageChops.difference(img2, img3).getbbox() #return None if no difference
        self.assertIsNotNone(res)



if __name__ == '__main__':
    unittest.main()
