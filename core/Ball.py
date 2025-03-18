from common import *

class Ball:
    def __init__(self, radius=5, padding=0, x=width / 2, y=height / 2, dx=3, dy=0, ax = 0, ay = 0, forces = []):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.ax, self.ay = ax,ay
        self.padding = padding
        self.radius = radius
        self.forces = forces

    def movecalc(self):
        self.dx += round(self.ax)
        self.dy += round(self.ay)
        self.x += round(self.dx)
        self.y += round(self.dy)

    def drawball(self):
        pygame.draw.circle(screen, col, (round(self.x), round(self.y)), self.radius + self.padding)