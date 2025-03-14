import pygame
import random

class Noise:
    def __init__(self, width: int, height: int):
        self.img = pygame.Surface((width, height))
        self.width, self.height = width, height
        self.points = [[(0) for x in range(width)] for y in range(height)]
    
    def genNoise(self):
        for y, _ in enumerate(self.points):
            for x, _ in enumerate(self.points[y]):
                if x != 0 and y != 0:
                    wanted = (random.uniform(-1,1) + 1.0) / 2
                    prevX = self.points[y][x - 1]
                    prevY = self.points[y - 1][x]
                    av = (wanted + prevX + prevY) / 3
                    self.points[y][x] = av
                elif (x == 0 or y == 0) and not (x == 0 and y == 0):
                    # get whether it's x that is 0 or y that is 0
                    if x == 0:
                        wanted = (random.uniform(-1,1) + 1.0) / 2
                        prev = self.points[y - 1][x]
                        av = (wanted + prev) / 2
                        self.points[y][x] = av
                    if y == 0:
                        wanted = (random.uniform(-1,1) + 1.0) / 2
                        prev = self.points[y][x - 1]
                        av = (wanted + prev) / 2
                        self.points[y][x] = av
                else:
                    self.points[y][x] = (random.uniform(-1,1) + 1.0) / 2
    
    def genImg(self, scale: int):
        for y, _ in enumerate(self.points):
            for x, item in enumerate(self.points[y]):
                col = int(255*item)
                self.img.set_at((x,y), (col, col, col))
        self.img = pygame.transform.scale(self.img, (self.width * scale, self.height * scale))