
import pygame

from thingy import Thingy

display = pygame.display.set_mode()

display.fill()

thing1 = Thingy(x=5, y=6, rotation=0)

def render(thingy, display):
    """ Render a thing 'thingy' onto the display """

    midpoint = display.get_height() // 2

    height = thingy.image.get_heigth()
    width = thingy.image.get_width()
    x = thingy.x
    y = midpoint - thingy.y

    coords = Rect(x, y, width, height)

    display.blit(thingy.image, coords)

render(thingy, display)



