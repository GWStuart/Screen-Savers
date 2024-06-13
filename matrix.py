import pygame
import random
pygame.init()

GRID_SIZE = 20
FONT_SIZE = 20
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPAWN_PROBABILITY = 500  # represents a 1 in x chance per column per frame
SNAKE_SPEED = 5

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

    def move(self):
        self.head += SNAKE_SPEED

    def draw(self):
        for i in range(self.length):
            character = random.choice(CHARACTERS)
            text = font.render(character, False, (0, 255, 0))
            win.blit(text, (GRID_SIZE*self.column + GRID_SIZE//2, self.head + GRID_SIZE*i + GRID_SIZE//2, GRID_SIZE, GRID_SIZE))

snakes = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            length, height = win.get_size()
            num_columns = length // GRID_SIZE

    for i in range(num_columns):
        # if 0 not in [snake.tail for snake in snakes if snake.column == i]:
        if random.randint(0, SPAWN_PROBABILITY) == 0:
            snakes.append(Snake(i, random.randint(3, 25)))

    win.fill((30, 30, 30))

    for snake in snakes:
        snake.move()
        if snake.head > height:
            snakes.remove(snake)
        snake.draw()

    pygame.display.update()
    clock.tick(60)

