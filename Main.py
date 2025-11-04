import pygame
from Grid import Grid
from Apple import Apple
from Snake import Snake

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake_move_interval = 150  # milliseconds per snake step
last_move_time = pygame.time.get_ticks()

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
grid = Grid(SCREEN_WIDTH-20,SCREEN_HEIGHT-20)
snake = Snake((0,25),grid)
num_apples = 1
apples = []
for i in range(num_apples):
    apple = Apple(grid)
    apples.append(apple)


# Running loop
run = True
while run:

    screen.fill((0,0,0))
    

    for apple in apples:
        pygame.draw.circle(screen, apple.color,(apple.x,apple.y), 6)


    for part in snake.body:
        pygame.draw.rect(screen, snake.color, part, 0)
        pygame.draw.rect(screen, (255,255,255), part, 2)


    # Check for wasd and update snake direction
    key = pygame.key.get_pressed()
    for keybind in keys_to_dir.keys():
        if key[keybind]:
            if keys_to_dir[keybind] % 2 == snake.direction[0] % 2:
                pass
            elif snake.can_turn(keys_to_dir[keybind]):
                snake.direction[0] = keys_to_dir[keybind]
                snake.last_turn_pos = (snake.body[0].x, snake.body[0].y)
    
    # for i,node in enumerate(snake.body):
    #     node.move_ip(dir_to_coord[snake.direction[i]])
    # snake.move()     

    current_time = pygame.time.get_ticks()
    snake.move()


    head = snake.body[0]
    for apple in apples:
        if abs(head.x + 10 - apple.x) < 20 and abs(head.y + 10 - apple.y) < 12:
            apple.eat()
            snake.grow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
    
    if snake.alive == False:
        break

    clock.tick(90)

    pygame.display.update()

# After running, quit
pygame.quit()


