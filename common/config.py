import pygame

# Render window
wsize = width, height = 250,250
scalesize = 30, 30
windowpad = 50
framerate = 60
screentoggle = False
screen = pygame.display.set_mode(wsize, flags=pygame.SCALED, vsync=1)

# Gravity
gmag = 1
degrees = 0
spinvel = 0

# Colours
col = (255,255,255)
bgcol = (0,0,0)

# Balls
rad = 6
pad = 0
padtoggle = True
bounciness = 0.6
bcount = 100