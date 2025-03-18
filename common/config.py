import pygame

# Render window
wsize = width, height = 250, 250
scalesize = 30, 30
windowpad = 0
framerate = 60
screentoggle = False
screen = pygame.display.set_mode(wsize, flags=pygame.SCALED, vsync=1)

# Gravity
gmag = 3
degrees = 90
spinvel = 0

# Colours
col = (255,255,255)
bgcol = (0,0,0)

# Balls
rad = 6
pad = 0
padtoggle = True
bounciness = 0.8
bcount = 100