import pygame

# Render window
width, height = 500, 500
pwidth, pheight = 1000,1000
scalesize = 500,500
windowpad = 0
framerate = 60
screentoggle = False
psurface = pygame.Surface((pwidth + (windowpad), pheight + (windowpad)))
screen = pygame.display.set_mode((width, height), flags=pygame.SCALED, vsync=1)

# Gravity
gmag = 8
deg = 90
spinvel = 0

# Colours
col2 = [255,255,255]
col = [0,0,0]
bgcol = [255,255,255]

# Balls
rad = 24
pad = 0
padtoggle = True
passes = 6
restitution = 0.9
friction = 0.8
bcount = 100
