import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 500
screen_height = 500

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set the font
font = pygame.font.SysFont(None, 25)

# Define the snake block size
block_size = 10

# Define the clock
clock = pygame.time.Clock()

# Define the function for displaying the message


def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [screen_width/6, screen_height/3])

# Define the function for drawing the snake


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Define the main game function


def game_loop():
    # Set the game over flag
    game_over = False

    # Set the game exit flag
    game_exit = False

    # Set the starting position of the snake
    lead_x = screen_width/2
    lead_y = screen_height/2

    # Set the initial movement of the snake
    lead_x_change = 0
    lead_y_change = 0

    # Generate the initial position of the food
    food_x = round(random.randrange(
        0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(
        0, screen_height - block_size) / 10.0) * 10.0

    # Initialize the snake list
    snake_list = []
    snake_length = 1

    # Game loop
    while not game_exit:

        while game_over:
            # Display the game over message
            screen.fill(white)
            message("Game over! Press Q to quit or C to play again", red)
            pygame.display.update()

            # Check for key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()

        # Check for key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
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

        # Update the position of the snake
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Check for collision with the boundaries
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_over = True

        # Create the snake head and body
        snake_head = []
        snake_head.append(lead_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with the snake body
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw the snake and the food on the screen
    screen.fill(white)
    pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
    snake(block_size, snake_list)

    # Update the snake length and the food position
    pygame.display.update()

    if lead_x == food_x and lead_y == food_y:
        food_x = round(random.randrange(
            0, screen_width - block_size) / 10.0) * 10.0
        food_y = round(random.randrange(
            0, screen_height - block_size) / 10.0) * 10.0
        snake_length += 1

    # Set the game FPS
    clock.tick(20)

game_loop()

# Quit Pygame and exit
pygame.quit()
quit()
