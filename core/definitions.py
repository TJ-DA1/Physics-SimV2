import math, random
from common import *

def boundary_difference(ball, vert, neg):
    if vert:
        if neg:
            return (ball.radius - ball.y) / ((ball.prevy - ball.y) if (ball.prevy - ball.y) > 0 else 0.01)
        else:
            return (ball.y - (pheight - ball.radius))  / ((ball.y - ball.prevy) if (ball.y - ball.prevy) > 0 else 0.01)
    else:
        if neg:
            return (ball.radius - ball.x) / ((ball.prevx - ball.x) if (ball.prevx - ball.x) > 0 else 0.01)
        else:
            return  (ball.x - (pwidth - ball.radius))  / ((ball.x - ball.prevx) if (ball.x - ball.prevx) > 0 else 0.01)

def create_ball(obj, num):
    return [obj(
        dx=random.uniform(-10, 10),
        dy=random.uniform(-10, 10),
        x=random.randint(0, pwidth),
        y=random.randint(0, pheight),
        radius=rad,
        padding = pad
    ) for _ in range(num)]

def resolve_forces(component):
    axtemp, aytemp = 0, 0
    for i in component:
        axtemp += i[0] * math.cos(math.radians(i[1]))
        aytemp += i[0] * math.sin(math.radians(i[1]))
    return round(axtemp, 2), round(aytemp,2)

def collide_check(b1,b2):
    if math.dist((b1.x, b1.y), (b2.x, b2.y)) <= b1.radius + b2.radius:
        return True
    else:
        return False

def collision_handle(b1, b2):
    diffx, diffy = b2.x - b1.x, b2.y - b1.y
    distance = math.dist((b1.x, b1.y), (b2.x, b2.y))
    overlap = b1.radius + b2.radius - distance

    if distance == 0:
        diffx = diffy = distance = 0.1

    nx, ny = diffx / distance, diffy / distance
    minoverlap = 1
    correction = max(overlap - minoverlap, 0) / 2

    b1.x -= (correction * nx)
    b1.y -= (correction * ny)
    b2.x += (correction * nx)
    b2.y += (correction * ny)

    collangle = math.atan2(diffy, diffx)
    b1norm = (b1.dx * math.cos(collangle)) + (b1.dy * math.sin(collangle))
    b1tan = (-1 * b1.dx * math.sin(collangle)) + (b1.dy * math.cos(collangle))
    b2norm = (b2.dx * math.cos(collangle)) + (b2.dy * math.sin(collangle))
    b2tan = (-1 * b2.dx * math.sin(collangle)) + (b2.dy * math.cos(collangle))

    b1normtemp = (((b1.rest - 1) * (b1norm)) + (((-1 * b1.rest) - 1) * (b2norm))) / -2
    b2normtemp = (((b1.rest + 1) * (b1norm)) + (((-1 * b1.rest) + 1) * (b2norm))) / 2
    b1norm, b2norm = b1normtemp, b2normtemp

    b1.dx = (b1norm * math.cos(collangle)) - (b1tan * math.sin(collangle))
    b1.dy = (b1norm * math.sin(collangle)) + (b1tan * math.cos(collangle))
    b2.dx = (b2norm * math.cos(collangle)) - (b2tan * math.sin(collangle))
    b2.dy = (b2norm * math.sin(collangle)) + (b2tan * math.cos(collangle))

