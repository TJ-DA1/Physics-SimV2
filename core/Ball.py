from common import *
from .definitions import *

class Ball:
    def __init__(self, radius=5, padding=0, x=width / 2, y=height / 2, dx=3, dy=0, ax = 0, ay = 0, forces = []):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.ax, self.ay = ax,ay
        self.padding = padding
        self.radius = radius
        self.forces = forces

    def movecalc(self, balls):
        for i in balls:
            if collide_check(self, i):
                collision_handle(self, i)

        if not (self.radius < self.y < height - self.radius):
            self.y, mplier = roundnearest(self.y, self.radius, height - self.radius)
            self.forces.append([-1 * resolve_forces(self.forces)[1], 90])
            self.dy = abs(self.dy) * mplier * bounciness
            self.dx *= bounciness

        if not (self.radius < self.x < width - self.radius):
            self.x, mplier = roundnearest(self.x, self.radius, width - self.radius)
            self.forces.append([resolve_forces(self.forces)[0], 180])
            self.dx = abs(self.dx) * mplier * bounciness
            self.dy *= bounciness

        for i in balls:
            if collide_check(self, i):
                collision_handle(self, i)

        self.dx += round(self.ax, 2)
        self.dy += round(self.ay, 2)

        self.x += round(self.dx, 2)
        self.y += round(self.dy, 2)



    def drawball(self):
        pygame.draw.circle(screen, col, (round(self.x, 2), round(self.y, 2)), self.radius + self.padding)