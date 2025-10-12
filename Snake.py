import pygame
from Apple import Apple
from Grid import Grid

class Snake:
    def __init__(self, initial_position: tuple, grid: Grid):
        self.body = [pygame.Rect((initial_position[0],initial_position[1],20,20))]  # List of tuples representing the snake's body segments
        self.direction = [1]
        self.size = 1  # Flag to indicate if the snake should grow
        self.color = (0, 255, 0)  # Green color for the snake
        self.grid = grid
        self.growing = False
        self.alive = True

    def move(self):
        if self.growing:
            self.grow()
            return
        
        for i in range(len(self.body)-1, -1, -1):
            # print(f"len {len(self.body)}, i = {i}")
            # i = (1-len(self.body)) - j
            if i > 0:
                # print(f"self.body[{i}] = self.body[{i - 1}]")
                self.body[i] = self.body[i - 1]
                self.direction[i] = self.direction[i]
                continue

            head_x, head_y = self.body[0][0:2]
            if self.direction[0] == 0:  # Up
                new_head = (head_x, head_y - 1)
            elif self.direction[0] == 1:  # Right
                new_head = (head_x + 1, head_y)
            elif self.direction[0] == 2:  # Down
                new_head = (head_x, head_y + 1)
            elif self.direction[0] == 3:  # Left
                new_head = (head_x - 1, head_y)
            else:
                raise ValueError("Invalid direction")
            self.body[0] = pygame.Rect((new_head[0],new_head[1],20,20))

            # Check if out of bounds
            test_grid = Grid(self.grid.size()[0], self.grid.size()[1])
            try: 
                test_grid.set_value(new_head[0], new_head[1], 1)
            except IndexError:
                self.lose()
                break
            
            # Check if hit self
            for i,node in enumerate(self.body):
                if i == 0: continue
                if self.body[0] == node:
                    self.lose()
                    break
                
                
        
    def grow(self):
        end_pos = self.body[-1]
        end_dir = self.direction[-1]
        self.growing = False
        for i in range(20):
            self.move()
        self.body.append(end_pos)
        self.direction.append(end_dir)

    def lose(self):
        self.alive = False
        print(f"Game Over. Score: {len(self.body)}")