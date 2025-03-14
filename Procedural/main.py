import pygame
import noise

pygame.init()

win = pygame.display.set_mode((600, 600))

# so how this is going to work i will divide the surface up into a grid this will be dubbed the in between method

n = noise.Noise(50, 50)
n.genNoise()
n.genImg(2 * 6)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((255, 255, 255))

    win.blit(n.img, (0, 0))

    pygame.display.update()

pygame.quit()