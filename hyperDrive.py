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

SPAWN_CHANCE = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3]

WHITE = (255, 255, 255)
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

def check_bounds(x, y, angle):
    if angle < math.pi / 2:
        return x > cx
    else:
        return x < cx

# dots are given as lists of (x, y, length, width, angle)
dots = [] # [[50, 10, 10, 3, calculate_angle(10, 10)]]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            run = False
        if event.type == pygame.VIDEORESIZE:
            length, height = win.get_size()
            cx, cy = length/2, height/2
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            dots.append([*mouse, 10, 3, calculate_angle(*mouse)])

    spawn = random.choice(SPAWN_CHANCE)
    for _ in range(spawn):
        width = random.randint(1, 4)
        plength = random.randint(2, 20)
        wall = random.randint(1, 4)
        if wall == 1:
            y = random.randint(0, height)
            dots.append([0, y, plength, width, calculate_angle(0, y)])
        elif wall == 2:
            y = random.randint(0, height)
            dots.append([length, y, plength, width, calculate_angle(length, y)])
        elif wall == 3:
            x = random.randint(0, length)
            dots.append([x, 0, plength, width, calculate_angle(x, 0)])
        else:
            x = random.randint(0, length)
            dots.append([x, height, plength, width, calculate_angle(x, height)])

    win.fill(BG)
    # pygame.draw.circle(win, (255, 0, 0), (cx, cy), 4)

    for dot in dots:
        pygame.draw.line(win, WHITE, (dot[0], dot[1]), move_point(dot[0], dot[1], dot[4], dot[2]), dot[3])
        dot[0], dot[1] = move_point(dot[0], dot[1], dot[4], dot[2])

        if check_bounds(*move_point(dot[0], dot[1], dot[4], dot[2]), dot[4]):  # check if it is past the centre
            dots.remove(dot)

    pygame.display.update()
    clock.tick(60)
