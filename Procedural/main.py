import pygame
import noise

pygame.init()

win = pygame.display.set_mode((600, 600))

# so how this is going to work i will divide the surface up into a grid this will be dubbed the in between method

n = noise.Noise(30, 30)
n.genNoise()
n.genImg(20)

hit_space = False

x, y = 0, 0

time = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    k = pygame.key.get_pressed()
    if k[pygame.K_SPACE] and not hit_space:
        n.genNoise()
        n.genImg(20)
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

    win.blit(n.img, (x, y))

    pygame.display.update()
    time.tick(60)

pygame.quit()