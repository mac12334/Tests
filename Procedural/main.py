import pygame
import noise
import image_reader

pygame.init()

# print(type(noise.pnoise2))

win = pygame.display.set_mode((600, 600))

hit_space = False

x, y = 0, 0
tiles = image_reader.get_tileset("Procedural/images/tileset.png", 3, 3, 16, 16, 2.34375)

def genNoise(width: int, height: int, seed: int, detail: int) -> list[list[float]]:
    scale = 500
    m = [[(0) for x in range(width)] for y in range(height)]
    for x in range(width):
        for y in range(height):
            m[y][x] = noise.pnoise2(x / scale, y / scale, detail, 0.6, 4, base = seed)
    return m

def getColor(val: float) -> pygame.Color:
    if val < 0:
        return (0, 0, 255)
    else:
        if val < 0.16:
            return (0, 255, 0)
        else:
            return (40, 40, 40)

def getImage(val: float) -> pygame.Surface:
    if val < 0:
        return tiles[1]
    else:
        if val < 0.16:
            return tiles[0]
        else:
            return tiles[2]

def getImageFromNoise(terrain: list[list[float]], width: int, height: int) -> pygame.Surface:
    image = pygame.Surface((width, height))
    for y in range(len(terrain)):
        for x in range(len(terrain[y])):
            tile = getImage(terrain[y][x])
            image.blit(tile, (tile.get_width() * x, tile.get_height() * y))
    return image

n = genNoise(16, 16, 100, 5)
image = getImageFromNoise(n, 600, 600)


time = pygame.time.Clock()
seed = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    k = pygame.key.get_pressed()
    if k[pygame.K_SPACE] and not hit_space:
        seed += 1
        n = genNoise(16, 16, seed + 100, 5)
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