from .definitions import *

class Ball:
    forces = []
    rest = restitution
    fric = friction
    def __init__(self, radius=5, padding=0, x=pwidth / 2, y=pheight / 2, dx=3, dy=0, ax = 0, ay = 0):
        self.x, self.y = x, y
        self.prevx, self.prevy = x, y
        self.dx, self.dy = dx, dy
        self.ax, self.ay = ax,ay
        self.padding = padding
        self.radius = radius
        self.yapply, self.xapply = True, True
        self.multix, self.multiy = 0.5, 0.5

    def movecalc(self):
        self.prevy, self.prevx = self.y, self.x
        self.multix, self.multiy = 0.5, 0.5
        self.yapply, self.xapply = True, True
        self.x += self.dx
        self.y += self.dy

    def movecalc2(self):
        self.ax, self.ay = resolve_forces(self.forces)
        if self.xapply:
            self.dx += self.ax
        else:
            self.dx += self.ax * self.multix
        if self.yapply:
            self.dy += self.ay
        else:
            self.dy += self.ay * self.multiy


    def boundarychecky(self):
        if not (self.radius <= self.y <= pheight - self.radius):
            if self.radius >= self.y:
                self.clipy = self.y
                self.y = self.radius
                self.dy = abs(self.dy) * self.fric
                self.multiy = boundary_difference(self, True, True)
                self.yapply = False

            else:
                self.clipy = self.y
                self.y = pheight - self.radius
                self.dy = abs(self.dy) * self.fric * -1
                self.multiy = boundary_difference(self, True, False)
                self.yapply = False
            self.dx *= self.fric

    def boundarycheckx(self):
        if not (self.radius <= self.x <= pwidth - self.radius):
            if self.radius >= self.x:
                self.clipx = self.x
                self.x = self.radius
                self.dx = abs(self.dx) * self.fric
                self.multix = boundary_difference(self, False, True)
                self.xapply = False

            else:
                self.clipx = self.x
                self.x = pwidth - self.radius
                self.dx = abs(self.dx) * self.fric * -1
                self.multix = boundary_difference(self, False, False)
                self.xapply = False
            self.dy *= self.fric

    def drawball(self, colour, colour2):
        pygame.draw.circle(psurface, colour2, (self.x + (windowpad / 2), self.y + (windowpad / 2)), self.radius + self.padding)
        pygame.draw.circle(psurface, colour, (self.x + (windowpad / 2), self.y + (windowpad / 2)), self.radius - math.ceil(self.radius / 5) + self.padding)