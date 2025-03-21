import pygame
import sys
import math
import datetime

pygame.init()
we, he = 1920, 1080
screen = pygame.display.set_mode((we, he))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

dial = pygame.image.load("clock.png").convert_alpha()
day = pygame.image.load("sun.jpg").convert()
night = pygame.image.load("moon.jpg").convert()
dial_r = dial.get_rect(center=(we // 2, he // 2))

hnd_m = pygame.image.load("min.png").convert_alpha()
hnd_s = pygame.image.load("sec.png").convert_alpha()
hnd_h = pygame.image.load("hour.png").convert_alpha()

font = pygame.font.SysFont("Arial", 48)

is_day = True
trans = False
start = 0.0
dur = 2.0

def ease(t):
    return -0.5 * (math.cos(math.pi * t) - 1)

def draw(img, angle):
    rot = pygame.transform.rotozoom(img, -angle, 1)
    rect = rot.get_rect(center=(we // 2, he // 2))
    screen.blit(rot, rect)

while True:
    dt = clock.tick(60) / 1000

    now = datetime.datetime.now()
    hour = now.hour
    new_day = 8 <= hour <= 20
    if new_day != is_day:
        is_day = new_day
        if not trans:
            trans = True
            start = pygame.time.get_ticks() / 1000


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    base = day if is_day else night
    over = night if is_day else day
    screen.blit(base, (0, 0))
    if trans:
        now_s = pygame.time.get_ticks() / 1000
        t = min((now_s - start) / dur, 1.0)
        a = int(ease(t) * 255)
        ovr = over.copy()
        ovr.set_alpha(255 - a)
        screen.blit(ovr, (0, 0))
        if t >= 1.0:
            trans = False
    screen.blit(dial, dial_r)

    sec = now.second + now.microsecond / 1_000_000
    minute = now.minute + sec / 60
    hour = (now.hour % 12) + minute / 60

    angle_s = sec * 6
    angle_m = minute * 6
    angle_h = hour * 30

    draw(hnd_h, angle_h)
    draw(hnd_m, angle_m)
    draw(hnd_s, angle_s)

    time_str = now.strftime("%H:%M:%S")
    text = font.render(time_str, True, (255, 255, 255))
    text_rect = text.get_rect(bottomright=(we - 30, he - 30))
    screen.blit(text, text_rect)

    pygame.display.flip()
