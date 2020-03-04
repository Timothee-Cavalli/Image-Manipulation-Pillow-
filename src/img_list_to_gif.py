#! /usr/bin/env python3
#-*- conding utf-8 -*-

from PIL import Image
import os

"""
This module contain the function:

-image_list_to_gif:
    Transform a list of pics into an animated gif


"""



def image_list_to_gif(img_list, path="new_gif.gif", duration=100, loop_mode=0):
    """
    Transform a list of Image into an animated gif
        -path : represente the path + name of the GIF
        -duration : how long is each frame (in milliseconds)
        -loop_mode : 0 = infinite loop, 1 = only once , 2 = twice ...
    """

    if not path.endswith(".gif"):
        path += ".gif"

    img_list[0].save(path, save_all=True, append_images=img_list[1:],
                        duration=duration, loop=loop_mode)


if __name__ == "__main__":
    import shuffling
    img_list = []
    print("Image list to gif : \n")
    img = Image.open("../image/spidey.jpg")
    for n in range(10):
        tmp = img.copy()
        shuffling.shuffling(tmp, 10)
        img_list.append(tmp)

    image_list_to_gif(img_list, "test")
    os.system("pause")
    os.remove("test.gif")
