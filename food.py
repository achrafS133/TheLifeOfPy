import pygame
import numpy as np

class Food:
    def __init__(self, x, y):
        self.pos = np.array([float(x), float(y)])
        self.radius = 3
        self.color = (0, 255, 0) # Green for food
        self.energy_value = 30.0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
