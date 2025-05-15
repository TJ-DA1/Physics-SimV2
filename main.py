from core  import *
import time

pygame.init()
etime = time.time()
balls = create_ball(Ball, bcount)
degrees = deg

for i in balls:
    i.listcoll, i.listcoll2 = setup_balls(balls, i)

running = True

def fixedupdate():
    global degrees
    degrees += spinvel
    psurface.fill(bgcol)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit

    gflip = -1 if keys[pygame.K_SPACE] else 1

    Ball.forces = [[gmag * gflip, degrees]]

    for _ in range(int(passes / 2)):
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if collide_check(balls[i], balls[j]):
                    collision_handle(balls[i], balls[j])

    for i in balls:
        i.movecalc()

    for _ in range(int(passes / 2)):
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if collide_check(balls[i], balls[j]):
                    collision_handle(balls[i], balls[j])

    for i in balls:
        i.movecalc()

    for i in balls:
        i.drawball()

    small_screen = pygame.transform.scale(psurface, scalesize)
    pixelated_screen = pygame.transform.scale(small_screen, (width, height))
    screen.blit(pixelated_screen, (0, 0))
    pygame.display.flip()


while running:
    dtime = time.time()
    if dtime - etime >= 1 / framerate:
        fixedupdate()
        etime += dtime - etime