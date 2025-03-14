import pygame
import random

class Noise:
    def __init__(self, width: int, height: int):
        self.img = pygame.Surface((width, height))
        self.points = [[(0) for x in range(width)] for x in range(height)]
        self.gridSpacing = (width // 2) + 1
    
    def genNoise(self):
        width = self.img.get_width() / self.gridSpacing
        print(self.gridSpacing)