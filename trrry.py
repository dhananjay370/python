import pygame
pygame.init()

# Specific Variable
width = 600
hight = 500
game_over = False
exit_game = False
snake_x = 45
snake_y = 55
fps = 30
snake_size = 10


# Colors
white = (255, 255, 255)
black = (0, 0, 0, 0)
red = (255, 0, 0, 0)

clock = pygame.time.Clock()

window = pygame.display.set_mode((width, hight))
pygame.display.set_caption("MyGame")
# pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x+10

    window.fill(white)
    pygame.draw.rect(window, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
