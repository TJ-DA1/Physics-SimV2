from core import *
import time
pygame.init()
time1 = time.time()

running = True
balls = Ball()
def fixedupdate():
    screen.fill((0,0,0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit

    balls.forces = [[1,90]]
    balls.ax = resolve_forces(balls.forces)[0]
    balls.ay = resolve_forces(balls.forces)[1]

    if not (balls.radius < balls.y < height - balls.radius):
        balls.y, mplier = roundnearest(balls.y, balls.radius, height - balls.radius)
        balls.dy = abs(balls.dy) * mplier * 1
        balls.dx *= 1

    if not (balls.radius < balls.x < width - balls.radius):
        balls.x, mplier = roundnearest(balls.x, balls.radius, width - balls.radius)
        balls.dx = abs(balls.dx) * mplier * 1
        balls.dy *= 1

    balls.movecalc()
    balls.drawball()
    screen.blit(screen, (0, 0))
    pygame.display.flip()

while True:
    dtime = time.time()
    if dtime - time1 >= 1 / framerate:
        fixedupdate()
        time1 += dtime - time1
