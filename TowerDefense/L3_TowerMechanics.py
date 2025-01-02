import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Setup
# TODO: Set the screen width to include a menu area
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MENU_WIDTH = # Your code here (hint: about 1/5 of screen width)
PLAY_AREA_WIDTH = # Your code here (hint: screen width minus menu width)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense: Tower Selection")

# Color Palette
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Tower Class for Menu and Placement
class Tower:
    def __init__(self, x, y, color, tower_type):
        """
        Create a tower with specific characteristics
        
        Parameters:
        - x: Tower's x-position
        - y: Tower's y-position
        - color: Tower's color
        - tower_type: Type of tower
        """
        # TODO: Set core tower attributes
        self.x = # Your code here
        self.y = # Your code here
        self.original_x = x  # Remember original menu position
        self.original_y = y
        self.color = # Your code here
        self.tower_type = # Your code here
        
        # Tower size
        self.size = 40
        
        # Flag to track if tower is being dragged
        self.is_held = False

    def draw(self, screen):
        """
        Draw the tower on the screen
        """
        # TODO: Draw the tower as a rectangle
        pygame.draw.rect(screen, # Color parameter
                         # Rectangle parameters (x, y, width, height)
                         )

    def is_hovered(self, mouse_pos):
            """
            Check if mouse is over the tower in the menu
            """
            # TODO: Implement hover detection
            # Hint: Check if mouse x,y is within tower's rectangle
            mx, my = mouse_pos
            #(# Condition for x-axis) (# Condition for y-axis)
            return (mx >= self.x and mx <= self.x + self.size and
                    my >= self.y and my <= self.y + self.size)

    def is_in_play_area(self):
        """
        Check if tower is in the playable area
        """
        # TODO: Implement play area detection
        return (self.x >= MENU_WIDTH and self.x <= SCREEN_WIDTH - self.size and
                self.y >= 0 and self.y <= SCREEN_HEIGHT - self.size)

# Main Game Loop
clock = pygame.time.Clock()
running = True

# Menu Towers
# TODO: Create a list of towers for the menu
menu_towers = [
    # First tower: Basic blue tower at menu position
    Tower(# x position in menu
          # y position in menu
          # color
          # tower type
    ),
    # Second tower: Different color and type
    Tower(# x position in menu
          # y position in menu
          # color
          # tower type
    )
]

# Variable to track which tower is being held
held_tower = None

while running:
    # Fill screen with white
    screen.fill(WHITE)
    
    # Draw menu background
    # TODO: Draw the menu area
    pygame.draw.rect(screen, # Color
                     # Rectangle parameters (0, 0, menu width, screen height)
                     )
    
    # Event handling
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            running = False
        
        # Mouse button down (picking up a tower)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # TODO: Check if a tower in the menu is clicked
            for tower in menu_towers:
                if tower.is_hovered(mouse_pos):
                    # Create a new tower to drag
                    held_tower = Tower(
                        mouse_pos[0],  # Current mouse x
                        mouse_pos[1],  # Current mouse y
                        tower.color,   # Same color as menu tower
                        tower.tower_type  # Same type as menu tower
                    )
                    held_tower.is_held = True
                    break
        
        # Mouse button up (placing the tower)
        elif event.type == pygame.MOUSEBUTTONUP:
            if held_tower:
                # TODO: Check if tower is in play area
                if held_tower.is_in_play_area():
                    # Tower is placed successfully
                    menu_towers.append(held_tower)
                
                # Reset held tower
                held_tower = None
        
        # Mouse motion (dragging tower)
        elif event.type == pygame.MOUSEMOTION:
            if held_tower:
                # TODO: Update held tower position
                held_tower.x = # Current mouse x
                held_tower.y = # Current mouse y
    
    # Draw menu towers
    for tower in menu_towers:
        tower.draw(screen)
    
    # Draw held tower if exists
    if held_tower:
        held_tower.draw(screen)
    
    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
