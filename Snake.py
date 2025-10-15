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
        self.speed = 2
        self.segment_size = 20
        self.positions = []  # <--- initialize here
        self.last_turn_pos = (self.body[0].x, self.body[0].y)


    def can_turn(self, new_dir):
        head = self.body[0]
        dx = abs(head.x - self.last_turn_pos[0])
        dy = abs(head.y - self.last_turn_pos[1])
        moved_distance = max(dx, dy)
        
        # Prevent 180° turns and require at least 1 segment distance
        if moved_distance >= self.segment_size and (self.direction[0] - new_dir) % 4 != 2:
            return True
        return False

    # def move(self):
    #     if self.growing:
    #         self.grow()
    #         return
        
    #     for i in range(len(self.body)-1, -1, -1):
    #         # print(f"len {len(self.body)}, i = {i}")
    #         # i = (1-len(self.body)) - j
    #         if i > 0:
    #             # print(f"self.body[{i}] = self.body[{i - 1}]")
    #             self.body[i] = self.body[i - 1]
    #             self.direction[i] = self.direction[i]
    #             continue

    #         head_x, head_y = self.body[0][0:2]
    #         if self.direction[0] == 0:  # Up
    #             new_head = (head_x, head_y - 20)
    #         elif self.direction[0] == 1:  # Right
    #             new_head = (head_x + 20, head_y)
    #         elif self.direction[0] == 2:  # Down
    #             new_head = (head_x, head_y + 20)
    #         elif self.direction[0] == 3:  # Left
    #             new_head = (head_x - 20, head_y)
    #         else:
    #             raise ValueError("Invalid direction")
    #         self.body[0] = pygame.Rect((new_head[0],new_head[1],20,20))

    #         # Check if out of bounds
    #         test_grid = Grid(self.grid.size()[0], self.grid.size()[1])
    #         try: 
    #             test_grid.set_value(new_head[0], new_head[1], 1)
    #         except IndexError:
    #             self.lose()
    #             break
            
    #         # Check if hit self
    #         for i,node in enumerate(self.body):
    #             if i == 0: continue
    #             if self.body[0] == node:
    #                 self.lose()
    #                 break

    def move(self):
        head = self.body[0]

        # Add current head position to history
        head_pos = (head.x, head.y)
        self.positions.insert(0, head_pos)

        # Update body segments to follow the head path
        for i, segment in enumerate(self.body[1:], start=1):
            frames_per_segment = int(self.segment_size / self.speed)
            index = i * frames_per_segment
            if index < len(self.positions):
                segment.x, segment.y = self.positions[index]

        # Then move the head normally according to direction
        if self.direction[0] == 0:
            head.y -= self.speed
        elif self.direction[0] == 1:
            head.x += self.speed
        elif self.direction[0] == 2:
            head.y += self.speed
        elif self.direction[0] == 3:
            head.x -= self.speed

        # Handle growth
        if self.growing:
            self.grow()
            self.growing = False
        
        # Check if out of bounds
        head = self.body[0]
        test_grid = Grid(self.grid.size()[0], self.grid.size()[1])
        try: 
            test_grid.set_value(head[0], head[1], 1)
        except IndexError:
            self.lose()
            
        
        # Check if hit self
        for segment in self.body[3:]:
            if head.colliderect(segment):
                self.lose()
                break
                
                
        
    # def grow(self):
    #     end_pos = self.body[-1]
    #     end_dir = self.direction[-1]
    #     self.growing = False
    #     for i in range(20):
    #         self.move()
    #     self.body.append(end_pos)
    #     self.direction.append(end_dir)

    # def grow(self):
    #     tail = self.body[-1].copy()
    #     self.body.append(tail)
    #     self.direction.append(self.direction[-1])

    def grow(self):
        tail = self.body[-1]
        direction = self.direction[-1]

        # Compute offset based on last direction (opposite of where it's moving)
        if direction == 0:   # Up → new tail below
            new_tail = pygame.Rect(tail.x, tail.y + 20, 20, 20)
        elif direction == 1: # Right → new tail to the left
            new_tail = pygame.Rect(tail.x - 20, tail.y, 20, 20)
        elif direction == 2: # Down → new tail above
            new_tail = pygame.Rect(tail.x, tail.y - 20, 20, 20)
        elif direction == 3: # Left → new tail to the right
            new_tail = pygame.Rect(tail.x + 20, tail.y, 20, 20)

        self.body.append(new_tail)
        self.direction.append(direction)

    def lose(self):
        self.alive = False
        print(f"Game Over. Score: {len(self.body)}")