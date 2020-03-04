#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os

"""
This module contain the function:

-black_and_white :
    Transform the image passed as parameter in a black and white Image,
    also called greyscale

"""


def black_and_white(img):
    """
    for each pixel of the img the average of it's RGB component is applied to
    each RGB component wich result in a darker or brighter grey
    """

    px = img.load()
    size_x, size_y = img.size


    for y in range (size_y):
        for x in range (size_x):
            ppx = px[x,y]
            average = int((ppx[0] + ppx[1] + ppx[2]) / 3)
            px[x,y] = (average, average, average)

def GreyScale(img):
    """ Same result but faster and not mine :/ """

    img.paste(img.convert("L"))


if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    print ("Black and White : \n")
    black_and_white(img)
    img.show()
    os.system("pause")
