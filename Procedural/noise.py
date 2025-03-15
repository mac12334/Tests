import pygame
import random

class Noise:
    def __init__(self, width: int, height: int):
        self.img = pygame.Surface((width, height))
        self.width, self.height = width, height
        self.points = [[(0) for x in range(width)] for y in range(height)]
    
    def makePronounced(self, value: float) -> float:
        if value < 0.5:
            value -= 0.04
        elif value > 0.5:
            value += 0.02
        if value < 0:
            value = 0
        elif value > 1:
            value = 1
        return value
    
    def smoothPixel(self, x: int, y: int) -> float:
        sur = []
        for h in range(3):
            for w in range(3):
                if h != 1 and w != 1:
                    # try and grab that piece of data if it's in range then good
                    if (w - 1 + x >= 0 and w - 1 + x <= self.width) and (h - 1 + y >= 0 and h - 1 + y <= self.height):
                        sur.append(self.points[h - 1][w - 1])
        
        # do the average
        sum = 0
        for i in sur:
            sum += i
        return (sum + self.points[y][x] + self.points[y][x]) / (len(sur) + 2)
    
    def genNoise(self):
        for y, _ in enumerate(self.points):
            for x, _ in enumerate(self.points[y]):
                if x != 0 and y != 0:
                    wanted = (random.uniform(-1,1) + 1.0) / 2
                    prevX = self.points[y][x - 1]
                    prevY = self.points[y - 1][x]
                    av = (wanted + prevX + prevY) / 3
                    av = self.makePronounced(av)
                    self.points[y][x] = av
                elif (x == 0 or y == 0) and not (x == 0 and y == 0):
                    # get whether it's x that is 0 or y that is 0
                    if x == 0:
                        wanted = (random.uniform(-1,1) + 1.0) / 2
                        prev = self.points[y - 1][x]
                        av = (wanted + prev) / 2
                        av = self.makePronounced(av)
                        self.points[y][x] = av
                    if y == 0:
                        wanted = (random.uniform(-1,1) + 1.0) / 2
                        prev = self.points[y][x - 1]
                        av = (wanted + prev) / 2
                        av = self.makePronounced(av)
                        self.points[y][x] = av
                else:
                    self.points[y][x] = (random.uniform(-1,1) + 1.0) / 2
        
        for y in range(self.height):
            for x in range(self.width):
                self.points[y][x] = self.smoothPixel(x, y) + random.uniform(-0.05, 0.05)

    def getAv(self) -> float:
        sum = 0
        for y in range(self.height):
            for x in range(self.width):
                sum += self.points[y][x]
        return sum / (self.width * self.height)
    
    def genImg(self, scale: int):
        av = self.getAv()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        for y, _ in enumerate(self.points):
            for x, item in enumerate(self.points[y]):
                col = int(255*item)
                if not item < av:
                    self.img.set_at((x,y), (0, col, 0))
                else:
                    self.img.set_at((x,y), (0, 0, col))
        self.img = pygame.transform.scale(self.img, (self.width * scale, self.height * scale))