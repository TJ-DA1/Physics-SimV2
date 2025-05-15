from common import *
from .definitions import *

class Ball:
    forces = []
    def __init__(self, radius=5, padding=0, x=pwidth / 2, y=pheight / 2, dx=3, dy=0, ax = 0, ay = 0):
        self.x, self.y = x, y
        self.prevx, self.prevy = x, y
        self.dx, self.dy = dx, dy
        self.ax, self.ay = ax,ay
        self.padding = padding
        self.radius = radius
        self.listcoll = []
        self.listcoll2 = []
        self.multix, self.multiy = 1,1

    def movecalc(self):
        self.x += self.dx / 2
        self.y += self.dy / 2
        self.multiy = self.boundarychecky()
        self.multix = self.boundarycheckx()

        self.ax, self.ay = resolve_forces(self.forces)

        self.dx += (self.ax / 2) * (self.multix if self.multix <= 1 else 1)
        self.dy += (self.ay / 2) * (self.multiy if self.multiy <= 1 else 1)

        self.prevx, self.prevy = self.x, self.y

    def boundarychecky(self):
        if not (self.radius <= self.y <= pheight - self.radius):
            if self.radius >= self.y:
                mpliery = boundary_difference(self, True, True)
                self.y = self.radius
                self.dy = abs(self.dy) * friction

            else:
                mpliery = boundary_difference(self, True, False)
                self.y = pheight - self.radius
                self.dy = abs(self.dy) * friction * -1

            self.dx *= friction
            return mpliery

        else:
            return 1

    def boundarycheckx(self):
        if not (self.radius <= self.x <= pwidth - self.radius):
            if self.radius >= self.x:
                mplierx = boundary_difference(self, False, True)
                self.x = self.radius
                self.dx = abs(self.dx) * friction

            else:
                mplierx = boundary_difference(self, False, False)
                self.x = pwidth - self.radius
                self.dx = abs(self.dx) * friction * -1

            self.dy *= friction
            return mplierx

        else:
            return 1

    def drawball(self):
        pygame.draw.circle(psurface, col, (self.x + (windowpad / 2), self.y + (windowpad / 2)), self.radius + self.padding)
        pygame.draw.circle(psurface, col2, (self.x + (windowpad / 2), self.y + (windowpad / 2)), self.radius - math.ceil(self.radius / 5) + self.padding)