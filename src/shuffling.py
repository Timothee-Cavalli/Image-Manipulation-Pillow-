#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
from random import sample
import os


"""
This module contain the function:

-shuffling : shuffle the picture with zone of size you want


"""

class ImgShuffling:
    """
    A class containing all the element necessary to do a shuffle effect
    """

    def __init__(self, img, crop_size):

        #actual pos on the pic
        self.x = 0
        self.y = 0
        #size of pic and zone
        self.crop_size = crop_size
        self.size_x, self.size_y = img.size
        self.end = False
        self.all_croped = []

        #lambda to avoid gooing too far on the line/column
        self.max_x = lambda x : self.x + self.crop_size if self.x + self.crop_size <= self.size_x else self.size_x
        self.max_y = lambda y : self.y + self.crop_size if self.y + self.crop_size <= self.size_y else self.size_y

    def add_crop(self, img):

        self.all_croped.append(img.crop((self.x, self.y, self.max_x(self.x), self.max_y(self.y))))

    def shuffle(self):

        self.all_croped = sample(self.all_croped, len(self.all_croped))

    def past_it(self, img):

        img.paste(self.all_croped[0], (self.x, self.y))

        del self.all_croped[0]

    def reset(self):
        self.x = 0
        self.y = 0
        self.end = False

    def next_line(self):
        self.x = 0
        self.y += self.crop_size

        if self.x >= self.size_x and self.y >= self.size_y:
            self.end = True

    def next_column(self):
        self.x += self.crop_size

        if self.x >= self.size_x and self.y >= self.size_y:
            self.end = True

    def end_line(self):

        return self.x >= self.size_x



def shuffling(img, crop_size):
    """
    The function for each zone of size crop_size attribute randomly
    another zone of crop_size
    """

    shuffly = ImgShuffling(img, crop_size)

    first_line = True
    nb = 0
    while (not shuffly.end):
        while(not shuffly.end_line()):
            nb = nb + 1 if first_line else nb
            shuffly.add_crop(img)
            shuffly.next_column()
        shuffly.next_line()
        first_line = False

    new_size_x = nb * crop_size
    new_size_y = int(len(shuffly.all_croped) / nb) * crop_size
    shuffled_img = Image.new("RGB", (new_size_x, new_size_y))

    shuffly.shuffle()
    shuffly.reset()
    while (not shuffly.end):
        while(not shuffly.end_line()):
            shuffly.past_it(shuffled_img)
            shuffly.next_column()
        shuffly.next_line()

    img.paste(shuffled_img)



if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")

    i = int(input("pixelisation size : "))
    shuffling(img, i)
    img.show()
    print ("shuffling: \n")
    os.system("pause")
