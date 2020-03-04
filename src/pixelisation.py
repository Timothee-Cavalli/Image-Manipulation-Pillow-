#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os


"""
This module contain the function:

-pixelisation :
    pixelise the picture with pixel of size you want


"""

class ImgPixelisation:
    """
    A class containing all the element necessary to do a pixelisation effect
    """

    def __init__(self, img, px_size):

        #actual pos on the pic
        self.x = 0
        self.y = 0
        #size of pic and zone
        self.px_size = px_size
        self.size_x, self.size_y = img.size
        #each pixel value (rgb)
        self.px = img.load()
        self.end = False
        self.avg = tuple

        #lambda to avoid gooing too far on the line/column
        self.max_x = lambda x : self.x + self.px_size if self.x + self.px_size <= self.size_x else self.size_x
        self.max_y = lambda y : self.y + self.px_size if self.y + self.px_size <= self.size_y else self.size_y

    def get_average(self):
        """ get the average of each RGB component of each pixel of the zone """

        sum = [0,0,0]
        nb = self.px_size * self.px_size
        for j in range(self.y, self.max_y(self.y)):
            for i in range(self.x, self.max_x(self.x)):
                sum[0] += self.px[i,j][0]
                sum[1] += self.px[i,j][1]
                sum[2] += self.px[i,j][2]

        self.avg = (round(sum[0] / nb), round(sum[1] / nb), round(sum[2] / nb))

    def fill(self):
        """ fill the zone"""

        for j in range(self.y, self.max_y(self.y)):
            for i in range(self.x, self.max_x(self.x)):
                self.px[i,j] = self.avg

    def next_line(self):
        self.x = 0
        self.y += self.px_size

        if self.x >= self.size_x and self.y >= self.size_y:
            self.end = True

    def next_column(self):
        self.x += self.px_size

        if self.x >= self.size_x and self.y >= self.size_y:
            self.end = True

    def end_line(self):
        return self.x >= self.size_x



def pixelisation(img, px_size):
    """
    The function for each zone of size px_size attribute the average color of
    each pixel of the zone
    """

    pixy = ImgPixelisation(img, px_size)

    while (not pixy.end):
        while(not pixy.end_line()):
            pixy.get_average()
            pixy.fill()
            pixy.next_column()
        pixy.next_line()





if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    i = int(input("pixelisation size : "))
    pixelisation(img, i)
    img.show()
    print ("pixelisation: \n")
    os.system("pause")
