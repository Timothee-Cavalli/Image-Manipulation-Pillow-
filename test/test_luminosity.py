#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image, ImageChops
import unittest
import sys
import os

sys.path.append("..\\src")

from luminosity import *


class LuminosityTest(unittest.TestCase):


    def test_luminosity_variation(self):

        img = Image.open("../image/spidey.jpg")
        img2 = Image.open("../image/spidey.jpg")
        img3 = Image.open("../image/spidey.jpg")
        size_x,size_y = img.size

        luminosity_variation(img, 50)
        luminosity_variation(img2, -50)
        luminosity_variation(img3, 100, True)

        darker = ImageChops.darker(img, img2) #get the darker pic
        res =  ImageChops.difference(darker, img2).getbbox() #return None if no difference
        self.assertIsNone(res)

        lighter = ImageChops.lighter(img, img3) #get the darker pic
        res =  ImageChops.difference(lighter, img3).getbbox() #return None if no difference
        self.assertIsNone(res)

        for y in range(size_y):
            for x in range(size_x):
                self.assertGreaterEqual(img.getpixel((x,y)), (50, 50, 50))
                self.assertLessEqual(img2.getpixel((x,y)), (205, 205, 205))
                self.assertEqual(img3.getpixel((x,y)), (255,255,255))


    def test_luminosity_percentage(self):

                img = Image.open("../image/spidey.jpg")
                img_clean = img.copy()
                img2 = Image.open("../image/spidey.jpg")
                img3 = Image.open("../image/spidey.jpg")
                size_x, size_y = img.size

                luminosity_percentage(img, 50)
                luminosity_percentage(img2, 0)
                luminosity_percentage(img3, 100)

                res =  ImageChops.difference(img, img_clean).getbbox() #return None if no difference
                self.assertIsNone(res)

                darker = ImageChops.darker(img, img2) #get the darker pic
                res =  ImageChops.difference(darker, img2).getbbox() #return None if no difference
                self.assertIsNone(res)

                lighter = ImageChops.lighter(img, img3) #get the darker pic
                res =  ImageChops.difference(lighter, img3).getbbox() #return None if no difference
                self.assertIsNone(res)


                for y in range (size_y):
                    for x in range (size_x):
                        self.assertTrue(img.getpixel((x,y)),img_clean.getpixel((x,y)))
                        self.assertTrue(img2.getpixel((x,y)), (0, 0, 0))
                        self.assertEqual(img3.getpixel((x,y)), (255,255,255))

if __name__ == '__main__':
    unittest.main()
