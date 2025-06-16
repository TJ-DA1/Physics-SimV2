import math, random
from common import *

def boundary_difference(ball, vert, neg):
    if vert:
        if neg:
            return (ball.radius - ball.clipy) / ((ball.prevy - ball.clipy) if (ball.prevy - ball.clipy) != 0 else 0.1)
        else:
            return (ball.clipy - (pheight - ball.radius))  / ((ball.clipy - ball.prevy) if (ball.clipy - ball.prevy) != 0 else 0.1)
    else:
        if neg:
            return (ball.radius - ball.clipx) / ((ball.prevx - ball.clipx) if (ball.prevx - ball.clipx) != 0 else 0.1)
        else:
            return (ball.clipx - (pwidth - ball.radius))  / ((ball.clipx - ball.prevx) if (ball.clipx - ball.prevx) != 0 else 0.1)

def create_ball(obj, num, radius):
    return [obj(
        dx=random.uniform(-10, 10),
        dy=random.uniform(-10, 10),
        x=random.randint(0, pwidth),
        y=random.randint(0, pheight),
        radius=radius,
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
        return True if b1 != b2 else False
    else:
        return False

def collision_overlap(b1, b2):
    diffx, diffy = b2.x - b1.x, b2.y - b1.y
    distance = math.dist((b1.x, b1.y), (b2.x, b2.y))
    overlap = b1.radius + b2.radius - distance

    if distance == 0:
        diffx =  0.1 if b2.prevx >= b1.prevx else -0.1
        diffy =  0.1 if b2.prevy >= b1.prevy else -0.1
        distance = 0.1

    nx, ny = diffx / distance, diffy / distance
    correction = overlap /  2

    b1.x -= (correction * nx)
    b1.y -= (correction * ny)
    b2.x += (correction * nx)
    b2.y += (correction * ny)

def collision_velocity(b1, b2):
    diffx, diffy = b2.x - b1.x, b2.y - b1.y
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

def hexformat(hexstring):
    validsep = [",", ".", " ", "/"]
    for i in validsep:
        if i in hexstring:
            string2 = hexstring
            string2 = string2.split(i)
            if len(string2) == 3:
                check = 0
                for i in string2:
                    try:
                        i = int(i)
                        if 0 <= i <= 255:
                            check += 1
                    except:
                        check = -1000000
                if check == 3:
                    return list([int(i) for i in string2])            
    return None