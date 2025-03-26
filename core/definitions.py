import math, random
from common import *

def create_ball(obj, num):
    return [obj(
        dx=random.uniform(-5, 0.5),
        dy=random.uniform(-0.5, 5),
        x=random.randint(0, width),
        y=random.randint(0, height),
        radius=rad,
        padding = pad
    ) for _ in range(num)]

def resolve_forces(component):
    axtemp, aytemp = 0, 0
    for i in component:
        axtemp += i[0] * math.cos(math.radians(i[1]))
        aytemp += i[0] * math.sin(math.radians(i[1]))
    return round(axtemp, 2), round(aytemp,2)

def setup_balls(blist, ball_):
    listtemp = list(blist)
    listtemp.remove(ball_)
    return listtemp

def round_nearest(val, x, y):
    distlist = [abs(val - x), abs(val - y)]
    lowest = distlist.index(min(distlist))
    return [x,y][lowest] + [1,-1][lowest], [1,-1][lowest]

def collide_check(b1,b2):
    if b1 == b2:
        return False
    elif math.dist((b1.x, b1.y), (b2.x, b2.y)) <= b1.radius + b2.radius:
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
    correction = overlap / 2

    b1.x -= (correction * nx)
    b1.y -= (correction * ny)
    b2.x += (correction * nx)
    b2.y += (correction * ny)

    collangle = math.atan2(diffy, diffx)
    b1norm = (b1.dx * math.cos(collangle)) + (b1.dy * math.sin(collangle))
    b1tan = (-1 * b1.dx * math.sin(collangle)) + (b1.dy * math.cos(collangle))
    b2norm = (b2.dx * math.cos(collangle)) + (b2.dy * math.sin(collangle))
    b2tan = (-1 * b2.dx * math.sin(collangle)) + (b2.dy * math.cos(collangle))

    b1norm, b2norm = restitution * b2norm, restitution * b1norm

    b1.dx = (b1norm * math.cos(collangle)) - (b1tan * math.sin(collangle))
    b1.dy = (b1norm * math.sin(collangle)) + (b1tan * math.cos(collangle))
    b2.dx = (b2norm * math.cos(collangle)) - (b2tan * math.sin(collangle))
    b2.dy = (b2norm * math.sin(collangle)) + (b2tan * math.cos(collangle))

