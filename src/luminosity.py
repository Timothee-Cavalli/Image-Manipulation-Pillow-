#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os


"""
This module contain the functions:

luminosity_variation:
    Change the luminosity of the image by the variation specified,
    the value stick between -255 and 255, or if percentage is true, between
    -100% and 100%

luminosity_percentage:
    Change the percentage luminosity of luminosity of the image :
        50 % = no change
        100 % = 100% luminosity
        0 % = 0% luminosity

Note: the variation are rights would be better if were curves

"""

def luminosity_variation(img, value, percentage=False):
    """
    The function for each pixel attribute the correct luminosity_variation.
    """

    if not percentage:
        mask = img.point(lambda i : i + value)
        img.paste(mask)

    else:
        mask = img.point(lambda i : i + round(value * 2.55))
        img.paste(mask)



def luminosity_percentage(img, percentage):
    """
    The function for each pixel attribute the correct luminosity_variation
    in percent.
    """

    if percentage < 0:
        percentage = 0

    if percentage > 100:
        percentage = 100

    mask = img.point(lambda i : i + round((percentage - 50) * 5.1))
    img.paste(mask)



if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    i = int(input("luminosity variation :"))
    luminosity_variation(img, i, 1)
    img.show()
    img = Image.open("../image/spidey.jpg")
    i = int(input("luminosity percentage :"))
    luminosity_percentage(img, i)
    img.show()
    os.system("pause")
