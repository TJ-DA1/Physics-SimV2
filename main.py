from core import *

context = SimulationContext()
context.balls = create_ball(Ball, bcount, rad)
running = True

def fixedupdate(ctx):
    ctx.deg += ctx.spinvel
    psurface.fill(ctx.bgcol)

    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    for event in events:
        if ctx.guitoggle:
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                ctx.colid = ["Main", "Outline", "Background"].index(event.selected_option_id)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                match ctx.colid:
                    case 0:
                        Ball.col = hexformat(event.text)
                    case 1:
                        Ball.col2 = hexformat(event.text)
                    case 2:
                        ctx.bgcol = hexformat(event.text)
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == gslider:
                    ctx.gmag = event.value
                    glabel.set_text(f"Gravity magnitude: {ctx.gmag}")
                elif event.ui_element == degslider:
                    ctx.deg = event.value + 90
                    deglabel.set_text(f"Gravity angle: {ctx.deg - 90}")
                elif event.ui_element == restslider:
                    Ball.rest = round(event.value, 0) / 10
                    restlabel.set_text(f"Restitution: {Ball.rest}")
                elif event.ui_element == fricslider:
                    Ball.fric = round(event.value, 0) / 10
                    friclabel.set_text(f"Friction: {Ball.fric}")
                elif event.ui_element == radslider:
                    for i in ctx.balls:
                        i.radius = event.value
                    radlabel.set_text(f"Radius: {ctx.balls[0].radius}")
                elif event.ui_element == ballcount:
                    if len(ctx.balls) < event.value:
                        ctx.balls += create_ball(Ball, event.value - len(ctx.balls), ctx.balls[0].radius)

                    elif len(ctx.balls) > event.value:
                        for i in range(len(ctx.balls) - event.value):
                            ctx.balls.pop()

                    config.bcount = len(ctx.balls)
                    balllabel.set_text(f"Balls: {config.bcount}")

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit
        manager.process_events(event)

    gflip = -1 if keys[pygame.K_SPACE] else 1
    Ball.forces = [[ctx.gmag * gflip, ctx.deg]]

    for i in ctx.balls:
        i.movecalc()

    for _ in range(passes):
        for i in range(len(ctx.balls)):
            for j in range(i + 1, len(ctx.balls)):
                b1, b2 = ctx.balls[i], ctx.balls[j]
                if collide_check(b1, b2):
                    collision_velocity(b1, b2)
                    collision_overlap(b1, b2)

        for ball in ctx.balls:
            ball.boundarycheckx()
            ball.boundarychecky()

    for i in ctx.balls:
        i.movecalc2()
        i.drawball(ball.col, ball.col2)

    if keys[pygame.K_g] and ctx.guiswitch:
        ctx.guitoggle = not ctx.guitoggle
        ctx.guiswitch = False
    elif not keys[pygame.K_g]:
        ctx.guiswitch = True

    small_screen = pygame.transform.scale(psurface, scalesize)
    pixelated_screen = pygame.transform.scale(small_screen, (width, height))
    screen.blit(pixelated_screen, (0, 0))

    if ctx.guitoggle:
        manager.update(dtime - ctx.etime)
        manager.draw_ui(screen)

    pygame.display.flip()

while running:
    dtime = time.time()
    if dtime - context.etime >= 1 / framerate:
        context.frames.append(1 / (dtime - context.etime))
        context.frames.pop(0)
        fixedupdate(context)
        framelabel.set_text(f"{round(sum(context.frames) / len(context.frames))}fps")
        context.etime += dtime - context.etime