#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os


"""
This module contain the function:

-sepia :
    add a sépia effect on the picture.

"""

def sepia(img, variation=(45,10,10)):
    """
    The function change the image in black_and_white and change according to
    variation parameter default: (45,10,10)
    """

    img.paste(img.convert("L"))
    px = img.load()

    size_x, size_y = img.size

    for y in range(size_y):
        for x in range(size_x):
            ppx = px[x,y]
            new = (ppx[0] + variation[0], ppx[1] + variation[1], ppx[2] + variation[2])
            px[x,y] = new




if __name__ == "__main__":
    img = Image.open("../image/merge_conflict.jpg")
    print ("Sepia: \n")
    sepia(img)
    img.show()
    os.system("pause")
