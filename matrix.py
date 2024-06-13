import pygame
import random
pygame.init()

GRID_SIZE = 20
FONT_SIZE = 20
a = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "01", "0123456789")
CHARACTERS = a[0]
SPAWN_PROBABILITY = 100  # represents a 1 in x chance per column per frame
CHARACTER_CHANGE_PROBABILITY = 10
SNAKE_SPEED = 6
SNAKE_LENGTH = (3, 25)

length, height = 800, 600
num_columns = length // GRID_SIZE

win = pygame.display.set_mode((length, height), pygame.RESIZABLE)
pygame.display.set_caption("Matrix")

clock = pygame.time.Clock()
font = pygame.font.SysFont('Sans', FONT_SIZE)

class Snake:
    def __init__(self, column, length):
        self.column = column
        self.length = length
        self.head = - length * GRID_SIZE
        self.characters = [random.choice(CHARACTERS) for _ in range(length)]

    def move(self):
        self.head += SNAKE_SPEED

    def draw(self):
        for i in range(self.length):
            if random.randint(0, CHARACTER_CHANGE_PROBABILITY) == 0:
                self.characters[i] = random.choice(CHARACTERS)
            text = font.render(self.characters[i], False, (0, 255, 0))
            win.blit(text, (GRID_SIZE*self.column + GRID_SIZE//2, self.head + GRID_SIZE*i + GRID_SIZE//2, GRID_SIZE, GRID_SIZE))

snakes = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            run = False
        if event.type == pygame.VIDEORESIZE:
            length, height = win.get_size()
            num_columns = length // GRID_SIZE

    for i in range(num_columns):
        if not any([snake.head < GRID_SIZE for snake in snakes if snake.column == i]):
            if random.randint(0, SPAWN_PROBABILITY) == 0:
                snakes.append(Snake(i, random.randint(*SNAKE_LENGTH)))

    win.fill((30, 30, 30))

    for snake in snakes:
        snake.move()
        if snake.head > height:
            snakes.remove(snake)
        snake.draw()

    pygame.display.update()
    clock.tick(60)
