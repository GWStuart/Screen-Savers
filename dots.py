import pygame
import random
import math
pygame.init()

SPWAN_CHANCE = 5
DOT_SIZE_RANGE = 5, 5
DOT_SPEED = 1
DRAW_RADIUS = 150

length, height = 800, 600
win = pygame.display.set_mode((length, height), pygame.RESIZABLE)
pygame.display.set_caption("Dots")

clock = pygame.time.Clock()

class Dot:
    COLOUR = (255, 255, 255)

    def __init__(self, x, y, r, direction):
        self.x = x
        self.y = y
        self.r = r
        self.direction = direction

    def move(self):
        self.x += math.cos(self.direction) * DOT_SPEED
        self.y += math.sin(self.direction) * DOT_SPEED

    def draw_lines(self):
        for dot in dots:
            dist = math.dist((self.x, self.y), (dot.x, dot.y))
            if dist < DRAW_RADIUS:
                p = dist / DRAW_RADIUS
                brightness = 255 - 100 * p**5
                colour = (brightness, brightness, brightness)
                strength = round(3 - 2 * p**5)
                pygame.draw.line(win, colour, (self.x, self.y), (dot.x, dot.y), strength)

    def draw(self):
        pygame.draw.circle(win, self.COLOUR, (self.x, self.y), self.r)

dots = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            run = False
        if event.type == pygame.VIDEORESIZE:
            length, height = win.get_size()

    if random.randint(0, SPWAN_CHANCE) == 0:
        r = random.randint(*DOT_SIZE_RANGE)
        wall = random.randint(1, 4)
        if wall == 1:
            x = -r
            y = random.randint(0, height)
            direction = random.uniform(-math.pi/2, math.pi/2)
        elif wall == 2:
            x = length + r
            y = random.randint(0, height)
            direction = random.uniform(math.pi/2, 3 * math.pi/2)
        elif wall == 3:
            x = random.randint(0, length)
            y = -r
            direction = random.uniform(0, math.pi)
        else:
            x = random.randint(0, length)
            y = height + r
            direction = random.uniform(-math.pi, 0)

        dots.append(Dot(x, y, r, direction))

    for dot in dots:
        dot.move()
        if dot.x > length + dot.r or dot.x < -dot.r:
            dots.remove(dot)
        elif dot.y > height + dot.r or dot.y < -dot.y:
            dots.remove(dot)

    win.fill((30, 30, 30))

    for dot in dots:
        dot.draw_lines()

    for dot in dots:
        dot.draw()

    pygame.display.update()
    clock.tick(60)
