import math, time

def resolve_forces(component):
    axtemp, aytemp = 0, 0
    for i in component:
        axtemp += i[0] * math.cos(math.radians(i[1]))
        aytemp += i[0] * math.sin(math.radians(i[1]))
    return round(axtemp), round(aytemp)

def roundnearest(val, x, y):
    distlist = [abs(val - x), abs(val - y)]
    lowest = distlist.index(min(distlist))
    return [x,y][lowest], [1,-1][lowest]