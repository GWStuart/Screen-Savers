import pygame
import random
import math
pygame.init()

length, height = 800, 600
cx, cy = length/2, height/2
win = pygame.display.set_mode((length, height), pygame.RESIZABLE)
pygame.display.set_caption("HyperDrive")

# SPAWN_CHANCE = 10  # represents a 1 in n chance per frame
# SPAWN_NUMBER = 5

SPEED = 0.4
SPAWN_CHANCE = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

FG = (255, 255, 255)
# FG = (255, 51, 51)
# FG = (51, 204, 255)
BG = (30, 30, 30)

clock = pygame.time.Clock()

def calculate_angle(x, y):
    dx = cx - x
    dy = cy - y
    if dx == 0:
        dx += 0.000001
    if (dx < 0):
        return math.atan(dy / dx) + math.pi
    return math.atan(dy / dx)

def move_point(x, y, angle, distance):
    return x + math.cos(angle)*distance, y + math.sin(angle)*distance

def get_tail(dot):
    if dot[5]:
        distance = math.dist((cx, cy), (dot[0], dot[1]))
        if (distance >= dot[3]):
            dot[5] = False
    else:
        distance = dot[3]
    return dot[0] - math.cos(dot[2])*distance, dot[1] - math.sin(dot[2])*distance

# dots are given as lists of (x, y, angle, length, width, bool_flag)
# the bool flag is True initially and is False when the point leaves the centre region
dots = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            elif event.key == pygame.K_UP:
                SPEED += 0.1
            elif event.key == pygame.K_DOWN:
                SPEED -= 0.1
        if event.type == pygame.VIDEORESIZE:
            length, height = win.get_size()
            cx, cy = length/2, height/2
            dots = []
        if event.type == pygame.MOUSEBUTTONDOWN:
            angle = random.random() * math.pi * 2
            dots.append([cx, cy, angle, 10, 3, True])

    spawn = random.choice(SPAWN_CHANCE)
    for _ in range(spawn):
        width = random.randint(1, 4)
        plength = random.randint(2, 20)
        angle = random.random() * math.pi * 2
        dots.append([cx, cy, angle, plength, width, True])

    win.fill(BG)

    for dot in dots:
        x, y = dot[0], dot[1]
        tx, ty = get_tail(dot)
        pygame.draw.line(win, FG, (x, y), (tx, ty), dot[4])
        dot[0], dot[1] = move_point(x, y, dot[2], dot[3] * SPEED)

        if tx > length or tx < 0 or ty > height or ty < 0:  # check if off screen
            dots.remove(dot)

    # Try uncomment these lines they look kind of cool
    # pygame.draw.circle(win, BG, (cx, cy), 15)
    # pygame.draw.circle(win, BG, (cx, cy), 50)
    # pygame.draw.circle(win, BG, (cx, cy), 15)
    # pygame.draw.circle(win, FG, (cx, cy), 15, 1)
    pygame.draw.circle(win, FG, (cx, cy), 2)

    pygame.display.update()
    clock.tick(60)
