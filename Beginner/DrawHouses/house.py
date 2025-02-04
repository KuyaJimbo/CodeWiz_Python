import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)  # Sky blue
GREEN = (34, 139, 34)   # Grass green
BROWN = (139, 69, 19)   # House base
RED = (178, 34, 34)     # Roof red
YELLOW = (255, 255, 0)  # Window yellow

# Function to draw the house
def draw_house():
    # Draw sky background
    screen.fill(BLUE)

    # Draw a rectangle template
    # pygame.draw.rect(screen, color, (x, y, width, height))

    # Draw grass
    pygame.draw.rect(screen, GREEN, (0, 300, screen_width, 100))

    # Draw the house base
    pygame.draw.rect(screen, BROWN, (200, 150, 200, 150))

    # Draw the roof
    pygame.draw.polygon(screen, RED, [(200, 150), (300, 80), (400, 150)])

    # Draw a door
    pygame.draw.rect(screen, BLACK, (275, 230, 50, 70))

    # Draw windows
    pygame.draw.rect(screen, YELLOW, (230, 180, 40, 40))  # Left window
    pygame.draw.rect(screen, YELLOW, (330, 180, 40, 40))  # Right window


while True:
    # Draw everything
    draw_house()
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
