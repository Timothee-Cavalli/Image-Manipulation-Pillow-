#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os


"""
This module contain the function:

-threshold : used to attribute 0 or 255

-thresholding : used to affect a threshold effect


"""

def threshold(value, i):
    """
    dependig to the value of i and value assigne or 0 or 255 can take a single
    value or a tuple of two element
    """

    if (isinstance(value, tuple)):
        if i > value[0] and i <= value [1]:
            return 255
        else:
            return 0

    if value < i:
        return 255
    else:
        return 0

def thresholding(img, value, choosed=""):
    """
    A function that affect a threshold effect on the image, can do it
    on the rgb componant individualy or on all of them is same time
    """

    if choosed: choosed = choosed.capitalize()
    try:
        if choosed in ("R", "G", "B"): R,G,B = img.split()
    except ValueError:
         R,G,B,A = img.split()


    if choosed == "R":
        R = R.point(lambda i : threshold(value, i))
        img.paste(R)

    elif choosed == "G":
        G = G.point(lambda i : threshold(value, i))
        img.paste(G)

    elif choosed == "B":
        B = B.point(lambda i : threshold(value, i))
        img.paste(B)

    else:
        mask = img.point(lambda i : threshold(value, i))
        img.paste(mask)



if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    i = int(input("threshold : "))
    a = input("choose : ")
    thresholding(img, i, a)
    img.show()
    os.system("pause")
