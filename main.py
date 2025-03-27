from core import *
import time

pygame.init()

time1 = time.time()

running = True
balls = create_ball(Ball, bcount)
degrees = deg

for i in balls:
    i.listcoll = setup_balls(balls, i)

def fixedupdate():
    global degrees
    degrees += spinvel
    screen.fill(bgcol)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit

    gflip = -1 if keys[pygame.K_SPACE] else 1

    for i in balls:
        for j in i.listcoll:
            if collide_check(i, j):
                collision_handle(i, j)

        i.forces = [[gmag * gflip, degrees]]
        i.movecalc()
        i.boundarycheck()

        for j in i.listcoll:
            if collide_check(i, j):
                collision_handle(i, j)

        i.drawball()

    screen.blit(screen, (0, 0))
    pygame.display.flip()

while running:
    dtime = time.time()
    if dtime - time1 >= 1 / framerate:
        fixedupdate()
        time1 += dtime - time1