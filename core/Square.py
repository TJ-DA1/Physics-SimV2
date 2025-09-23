import random
from .definitions import *

class Square:
    col = col
    col2 = col2
    rest = restitution
    fric = friction
    def __init__(self, x = pwidth / 2, y = pheight / 2, angle = 45, size = 200):
        self.x, self.y = x, y
        self.angle = angle
        self.size = size
        self.lines = []

    def drawsquare(self):
        pygame.draw.polygon(psurface, col2, self.points, 5)
