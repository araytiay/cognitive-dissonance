
import pygame

from thingy import Thingy

display = pygame.display.set_mode()

thing1 = Thingy(x=5, y=6, rotation=0)

def render(thingy, display):
    """ Render a thing 'thingy' onto the display """

    midpoint = display.get_height() // 2

    display.blit(thing1.image, Rect(0, 0, thing1.width, thing1.height))

render(thingy, display)



