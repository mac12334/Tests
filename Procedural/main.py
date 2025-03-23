import pygame
import noise
import image_reader
import random

pygame.init()

# print(type(noise.pnoise2))

win = pygame.display.set_mode((600, 600))

hit_space = False

x, y = 0, 0
tiles = image_reader.get_tileset("Procedural/images/tileset.png", 3, 3, 16, 16, 2.34375)
seed = random.randint(-100, 100)

def genNoise(width: int, height: int, seed: int, detail: int, x_off: int, y_off: int) -> list[list[float]]:
    scale = 500
    m = [[(0) for x in range(width)] for y in range(height)]
    for x in range(width):
        for y in range(height):
            m[y][x] = noise.pnoise2((x + x_off) / scale, (y + y_off) / scale, detail, 0.6, 4, base = seed)
    return m

def inRange(start: float, val: float, end: float) -> bool:
    return start <= val < end

def getImage(val: float) -> pygame.Surface:
    if inRange(-1, val, 0):
        return tiles[1]
    if inRange(0, val, 0.15):
        return tiles[0]
    if inRange(0.15, val, 0.23):
        return tiles[3]
    return tiles[2]

def getImageFromNoise(terrain: list[list[float]], width: int, height: int) -> pygame.Surface:
    image = pygame.Surface((width, height))
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            tile = getImage(terrain[y][x])
            image.blit(tile, (tile.get_width() * x, tile.get_height() * y))
    return image

n = genNoise(20, 20, seed, 8, x, y)
image = getImageFromNoise(n, 600 + 2 * (4.6 * 16), 600 + 2 * (4.6 * 16))
pressed = False

p_x, p_y = 300 - 25, 300 - 25
player = pygame.Rect(p_x, p_y, 50, 50)
w_x,w_y = -4.6 * 16, -4.6 * 16

time = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    k = pygame.key.get_pressed()
    if k[pygame.K_w] and not pressed:
        w_y += 5
    if k[pygame.K_a] and not pressed:
        w_x += 5
    if k[pygame.K_s] and not pressed:
        w_y -= 5
    if k[pygame.K_d] and not pressed:
        w_x -= 5

    if w_x > -2.3 * 16:
        w_x = -4.6 * 16
        x -= 1
        n = genNoise(20, 20, seed, 8, x, y)
        image = getImageFromNoise(n, 600 + 2 * (4.6 * 16), 600 + 2 * (4.6 * 16))
    if w_x < (-2.3 * 3) * 16:
        w_x = -4.6 * 16
        x += 1
        n = genNoise(20, 20, seed, 8, x, y)
        image = getImageFromNoise(n, 600 + 2 * (4.6 * 16), 600 + 2 * (4.6 * 16))
    if w_y > -2.3 * 16:
        w_y = -4.6 * 16
        y -= 1
        n = genNoise(20, 20, seed, 8, x, y)
        image = getImageFromNoise(n, 600 + 2 * (4.6 * 16), 600 + 2 * (4.6 * 16))
    if w_y < (-2.3 * 3) * 16:
        w_y = -4.6 * 16
        y += 1
        n = genNoise(20, 20, seed, 8, x, y)
        image = getImageFromNoise(n, 600 + 2 * (4.6 * 16), 600 + 2 * (4.6 * 16))
    win.fill((255, 255, 255))

    win.blit(image, (w_x, w_y))
    pygame.draw.rect(win, (255, 0, 0), player)

    pygame.display.update()
    time.tick(60)

pygame.quit()