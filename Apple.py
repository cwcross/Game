from Grid import Grid
import random
import pygame
class Apple:
    def __init__(self, grid: Grid):
        self.x_max = grid.cols - 1
        self.y_max = grid.rows - 1

        self.x = random.randint(0, self.x_max)
        self.y = random.randint(0, self.y_max)
        self.color = (255, 0, 0)  # Red color for the apple
        self.grid = grid
    
    def eat(self):
        self.x = random.randint(10, self.x_max)
        self.y = random.randint(10, self.y_max)
        