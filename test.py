import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create object on screen
player = pygame.Rect((300,250,50,50))

# Running loop
run = True
while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    if key[pygame.K_d] == True:
        player.move_ip(1,0)
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    if key[pygame.K_s] == True:
        player.move_ip(0,1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
    
    pygame.display.update()

# After running, quit
pygame.quit()
