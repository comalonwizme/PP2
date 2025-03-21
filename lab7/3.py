import pygame

pygame.init()

we, he = 800, 800
radius = 25
color = (255, 0, 0)
bg = (255, 255, 255)
step = 20

screen = pygame.display.set_mode((we, he))
pygame.display.set_caption("Redball")

x, y = he // 2, we // 2

ok = True
while ok:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + radius + step <= we:
        x += step
    if keys[pygame.K_UP] and y - radius - step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + radius + step <= he:
        y += step

    screen.fill(bg)
    pygame.draw.circle(screen, color, (x, y),  radius)
    pygame.display.update()
pygame.quit()
