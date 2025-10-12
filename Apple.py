from Grid import Grid
import random
class Apple:
    def __init__(self, grid: Grid):
        self.x_max = grid.cols - 1
        self.y_max = grid.rows - 1

        self.x = random.randint(0, self.x_max)
        self.y = random.randint(0, self.y_max)
        self.color = (255, 0, 0)  # Red color for the apple
        self.grid = grid
    
    def eat(self):
        self.grid.set_value(self.x, self.y, 0)  # Assuming 0 means empty cell
        self = Apple(self.grid)  # Reinitialize to get a new position
        