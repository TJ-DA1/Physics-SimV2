from common import *
from .definitions import *

class Ball:
    def __init__(self, radius=5, padding=0, x=pwidth / 2, y=pheight / 2, dx=3, dy=0, prevdx = 0, prevdy = 0, ax = 0, ay = 0, forces = [], listcoll = [], listcoll2 = []):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.prevdx, self.prevdy = prevdx, prevdy
        self.ax, self.ay = ax,ay
        self.padding = padding
        self.radius = radius
        self.forces = forces
        self.listcoll = listcoll
        self.listcoll2 = listcoll2

    def movecalc(self):
        self.x += round(self.dx) / 2
        self.y += round(self.dy) / 2
        self.ax, self.ay = resolve_forces(self.forces)[0] / 2, resolve_forces(self.forces)[1] / 2
        self.prevdx = self.dx
        self.prevdy = self.dy
        self.dx += self.ax / 2
        self.dy += self.ay / 2

    def boundarycheck(self):
        if not (self.radius <= self.y <= pheight - self.radius):
            self.y, mplier = round_nearest(self.y, self.radius, pheight - self.radius)
            #self.forces.append([mplier * abs(resolve_forces(self.forces)[1]), 90])
            print(self.dy)
            self.dy = math.floor(math.sqrt((self.prevdy)**2 * friction) * mplier)
            print(self.dy)
            self.dx *= friction

        if not (self.radius <= self.x <= pwidth - self.radius):
            self.x, mplier = round_nearest(self.x, self.radius, pwidth - self.radius)
            #self.forces.append([mplier * abs(resolve_forces(self.forces)[0]), 0])
            print(self.dx)
            self.dx = math.floor(math.sqrt((self.prevdx**2) * friction) * mplier)
            print(self.dx)
            self.dy *= friction

    def drawball(self):
        pygame.draw.circle(psurface, col, (self.x + (windowpad / 2), self.y + (windowpad / 2)), self.radius + self.padding)
        pygame.draw.circle(psurface, col2, (self.x + (windowpad / 2), self.y + (windowpad / 2)),self.radius - 5+ self.padding)