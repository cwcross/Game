import pygame
from Grid import Grid
from Apple import Apple
from Snake import Snake

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

keys_to_dir = {
        pygame.K_w:0,
        pygame.K_d:1,
        pygame.K_s:2,
        pygame.K_a:3
    }

dir_to_coord = {
        0:(0,-1),
        1:(1,0),
        2:(0,1),
        3:(-1,0)
    }

# Create object on screen
grid = Grid(SCREEN_WIDTH,SCREEN_HEIGHT)
snake = Snake((0,25),grid)

# Running loop
run = True
while run:

    screen.fill((0,0,0))

    

    for part in snake.body:
        pygame.draw.rect(screen, snake.color, part)

    # Check for wasd and update snake direction
    key = pygame.key.get_pressed()
    for keybind in keys_to_dir.keys():
        if key[keybind]:
            if keys_to_dir[keybind] % 2 == snake.direction[0] % 2:
                pass
            else:
                snake.direction[0] = keys_to_dir[keybind]
    
    for i,node in enumerate(snake.body):
        node.move_ip(dir_to_coord[snake.direction[i]])
    snake.move()      

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
    
    if snake.alive == False:
        break
    
    pygame.display.update()

# After running, quit
pygame.quit()


