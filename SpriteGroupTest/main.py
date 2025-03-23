import pygame

pygame.init()

width, height = 600, 600
win = pygame.display.set_mode((width, height))

class Object(pygame.sprite.Sprite):
    def __init__(self, is_player: bool = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.is_player = is_player
        self.speed = 4
    def update(self) -> None:
        if self.is_player:
            dx, dy = 0, 0
            k = pygame.key.get_pressed()
            if k[pygame.K_w]:
                dy -= self.speed
            if k[pygame.K_a]:
                dx -= self.speed
            if k[pygame.K_s]:
                dy += self.speed
            if k[pygame.K_d]:
                dx += self.speed
            if ((dx**2 + dy**2)**(1/2) != self.speed) and ((dx != 0) and (dy != 0)):
                dx = (dx * (2**(1/2))) / 2
                dy = (dy * (2**(1/2))) / 2
            self.rect.x += dx
            self.rect.y += dy

block = Object(True)
g = pygame.sprite.Group()
g.add(block)

run = True
clock = pygame.time.Clock()
while run:
    win.fill((255, 255, 255))

    g.update()
    g.draw(win)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
pygame.quit()