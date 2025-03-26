from core import *
import time

pygame.init()

time1 = time.time()

balls = create_ball(Ball, bcount)
degrees = deg

for i in balls:
    i.listcoll = setup_balls(balls, i)

c1 = 0
c2 = 1
up = True

def fixedupdate():
    global degrees, c1, c2, up
    degrees += spinvel
    screen.fill((0, 0, 0))
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

    if up:
        col[c2] += 2
        if col[c2] >= 255:
            col[c2] = 255
            up = not up
    else:
        col[c1] -= 2
        if col[c1] <= 0:
            col[c1] = 0
            up = not up
            c1 += 1 if c1 != 2 else -2
            c2 += 1 if c2 != 2 else -2

    print(col)


while True:
    dtime = time.time()
    if dtime - time1 >= 1 / framerate:
        fixedupdate()
        time1 += dtime - time1
