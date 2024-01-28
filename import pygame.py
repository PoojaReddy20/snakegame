import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake initial position and properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"

# Food initial position
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        snake_direction = "RIGHT"
    if keys[pygame.K_LEFT]:
        snake_direction = "LEFT"
    if keys[pygame.K_UP]:
        snake_direction = "UP"
    if keys[pygame.K_DOWN]:
        snake_direction = "DOWN"

    # Move the snake
    if snake_direction == "RIGHT":
        snake_pos[0] += 10
    if snake_direction == "LEFT":
        snake_pos[0] -= 10
    if snake_direction == "UP":
        snake_pos[1] -= 10
    if snake_direction == "DOWN":
        snake_pos[1] += 10

    # Snake body mechanics
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    # Render the screen
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        pygame.quit()
        sys.exit()
    if snake_pos in snake_body[1:]:
        pygame.quit()
        sys.exit()

    # Refresh screen
    pygame.display.update()
    clock.tick(15)  # Frame rate

if __name__ == "__main__":
    main()
