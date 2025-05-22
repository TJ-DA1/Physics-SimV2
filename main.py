from core import *
import time

etime = time.time()
balls = create_ball(Ball, bcount, rad)
guitoggle = True
guiswitch = True
frames = [framerate for i in range(5)]

running = True

def fixedupdate():
    global guitoggle, guiswitch, gmag, deg, friction, restitution, balls
    deg += spinvel
    psurface.fill(bgcol)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if guitoggle:
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == gslider:
                    gmag = event.value
                    glabel.set_text(f"Gravity magnitude: {gmag}")
                elif event.ui_element == degslider:
                    deg = event.value + 90
                    deglabel.set_text(f"Gravity angle: {deg - 90}")
                elif event.ui_element == restslider:
                    restitution = round(event.value, 0) / 10
                    restlabel.set_text(f"Restitution: {restitution}")
                elif event.ui_element == fricslider:
                    friction = round(event.value, 0) / 10
                    friclabel.set_text(f"Friction: {friction}")
                elif event.ui_element == radslider:
                    for i in balls:
                        i.radius = event.value
                    radlabel.set_text(f"Radius: {balls[0].radius}")
                elif event.ui_element == ballcount:
                    if len(balls) < event.value:
                        balls += create_ball(Ball, event.value - len(balls), balls[0].radius)

                    elif len(balls) > event.value:
                        for i in range(len(balls) - event.value):
                            balls.pop()

                    config.bcount = len(balls)
                    balllabel.set_text(f"Balls: {config.bcount}")

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit
        manager.process_events(event)

    gflip = -1 if keys[pygame.K_SPACE] else 1

    if keys[pygame.K_g] and guiswitch:
        guitoggle = not guitoggle
        guiswitch = False

    elif not keys[pygame.K_g]:
        guiswitch = True

    Ball.forces = [[gmag * gflip, deg]]
    Ball.rest = restitution
    Ball.fric = friction

    for i in balls:
        i.movecalc()

    for _ in range(passes):

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                b1, b2 = balls[i], balls[j]
                if collide_check(b1, b2):
                    collision_velocity(b1, b2)
                    collision_overlap(b1, b2)

        for ball in balls:
            ball.boundarycheckx()
            ball.boundarychecky()


    for i in balls:
        i.movecalc2()
        i.drawball()

    manager.update(dtime - etime)

    small_screen = pygame.transform.scale(psurface, scalesize)
    pixelated_screen = pygame.transform.scale(small_screen, (width, height))
    screen.blit(pixelated_screen, (0, 0))
    if guitoggle:
        manager.draw_ui(screen)
    pygame.display.flip()
while running:
    dtime = time.time()
    if dtime - etime >= 1 / framerate:
        frames.append(1 / (dtime - etime))
        frames.pop(0)
        fixedupdate()
        framelabel.set_text(f"{round(sum(frames) / len(frames))}fps")
        etime += dtime - etime