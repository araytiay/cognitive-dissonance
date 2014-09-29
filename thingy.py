#! /usr/local/bin/python3.4

import pygame

global DEFAULT
#DEFAULT = open("4_5_degrees copy.png")
#I did what?!
DEFAULT = pygame.image.open("4_5_degrees copy.png")

class Thingy():

    """This is our object thing"""

    def __init__(self, x, y, rotation, image=DEFAULT):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.image = image

    #wait wait wait what is this?
    #hehehe Oh no
    #I am being annoying now... sorry
