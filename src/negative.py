#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os


"""
This module contain the function:

-negative :
    Transform the image passed as parameter in a negative Image,
    it work pretty well and is very quick thanks to the point function

"""

def negative(img):
    """
    The function for each pixel attribute the invserse color
    """

    mask = img.point(lambda i : 255 - i)
    img.paste(mask)



if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    negative(img)
    img.show()
    print ("Negative: \n")
    os.system("pause")
