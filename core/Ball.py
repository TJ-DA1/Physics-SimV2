from common import *
from .definitions import *

class Ball:
    def __init__(self, radius=5, padding=0, x=width / 2, y=height / 2, dx=3, dy=0, ax = 0, ay = 0, forces = [], listcoll = []):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.ax, self.ay = ax,ay
        self.padding = padding
        self.radius = radius
        self.forces = forces
        self.listcoll = listcoll

    def movecalc(self):
        self.ax = resolve_forces(self.forces)[0]
        self.ay = resolve_forces(self.forces)[1]

        self.dx += self.ax
        self.dy += self.ay

        self.x += self.dx
        self.y += self.dy

    def boundarycheck(self):
        if not (self.radius < self.y < height - self.radius):
            self.y, mplier = round_nearest(self.y, self.radius, height - self.radius)
            self.forces.append([mplier * abs(resolve_forces(self.forces)[1]), 90])
            self.dy = abs(self.dy) * mplier * restitution
            self.dx *= restitution

        if not (self.radius < self.x < width - self.radius):
            self.x, mplier = round_nearest(self.x, self.radius, width - self.radius)
            self.forces.append([mplier * abs(resolve_forces(self.forces)[0]), 0])
            self.dx = abs(self.dx) * mplier * restitution
            self.dy *= restitution

    def drawball(self):
        pygame.draw.circle(screen, col, (self.x, self.y), self.radius + self.padding)