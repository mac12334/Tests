import pygame
import noise
import random

pygame.init()

# print(type(noise.pnoise2))

win = pygame.display.set_mode((600, 600))

hit_space = False

x, y = 0, 0

def genNoise(width: int, height: int, seed: int) -> list[list[float]]:
    m = [[(0) for x in range(width)] for y in range(height)]
    for x in range(width):
        for y in range(height):
            m[y][x] = noise.pnoise2((x + 1) / 200, (y + 1) / 200, 6, 0.6, 4, base = seed)
    return m

def getImageFromNoise(terrain: list[list[float]], width: int, height: int) -> pygame.Surface:
    image = pygame.Surface((len(terrain[0]), len(terrain)))
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            if terrain[y][x] > 0:
                val = (0, 255, 0)
            else:
                val = (0, 0, 255)
            image.set_at((x, y), val)
    image = pygame.transform.scale(image, (width, height))
    return image

n = genNoise(600, 600, random.randint(0, 100))
image = getImageFromNoise(n, 600, 600)

time = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    k = pygame.key.get_pressed()
    if k[pygame.K_SPACE] and not hit_space:
        n = genNoise(600, 600, random.randint(0, 100))
        image = getImageFromNoise(n, 600, 600)
        hit_space = True
    if not k[pygame.K_SPACE]:
        hit_space = False

    if k[pygame.K_w]:
        y += 5
    if k[pygame.K_a]:
        x += 5
    if k[pygame.K_s]:
        y -= 5
    if k[pygame.K_d]:
        x -= 5
    win.fill((255, 255, 255))

    win.blit(image, (x, y))

    pygame.display.update()
    time.tick(60)

pygame.quit()