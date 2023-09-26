import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set the game clock
clock = pygame.time.Clock()

# Set the font for the game messages
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    """
    Function to display a message on the screen
    """
    message = font_style.render(msg, True, color)
    screen.blit(message, [screen_width / 6, screen_height / 3])


def snake(block_size, snake_list):
    """
    Function to draw the snake on the screen
    """
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block_size, block_size])


def game_loop():
    """
    Function to run the main game loop
    """
    game_over = False
    game_close = False

    # Set the initial position and movement direction of the snake
    lead_x = screen_width / 2
    lead_y = screen_height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Set the dimensions of the food and the snake blocks
    block_size = 10

    # Set the initial position of the food
    food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Set the initial length of the snake
    snake_list = []
    snake_length = 1

    # Run the game loop
    while not game_over:

        # Check for game events
        while game_close:
            screen.fill(white)
            message("You lost! Press C to play again or Q to quit", red)
            pygame.display.update()

            # Check for key presses
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Check for collision with the boundaries
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_close = True

        # Update the snake position
        lead_x += lead_x_change
        lead_y += lead_y_change
        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)

        # Check for collision with the food
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            snake_length += 1

        # Remove the tail of the snake if it is too long
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with the snake body
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Fill the screen with white
        screen.fill(white)

        # Draw the food on the screen
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        # Draw the snake on the screen
        snake(block_size, snake_list)
        pygame.display.update()

        # Set the game speed
        clock.tick(20)

    # Quit Pygame
    pygame.quit()

    # Quit Python
    quit()

# Run the game loop
game_loop()

        # Create the snake head
