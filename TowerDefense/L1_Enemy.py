import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Setup (Fill in the blanks!)
# TODO: Set the screen width and height
SCREEN_WIDTH = # Your code here
SCREEN_HEIGHT = # Your code here

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Tower Defense Game")

# Color Palette - Make the game look cool!
# TODO: Define some colors using RGB values
# Hint: Colors are created like (Red, Green, Blue) with values from 0-255
WHITE = # Your color here (hint: maximum brightness)
BLACK = # Your color here (hint: no brightness)
RED = # Your color here (hint: full red)

# Enemy Class - The bad guys in our game!
class Enemy:
    def __init__(self, x, y, health, speed, color):
        """
        Create an enemy with these characteristics:
        - x: Starting x-position
        - y: Starting y-position
        - health: How many hits it can take
        - speed: How fast it moves
        - color: What color the enemy appears
        """
        # TODO: Use the input parameters to set up the enemy's attributes
        # Hint: Use 'self' to create instance variables
        self.x = # Your code here
        self.y = # Your code here
        self.health = # Your code here
        self.speed = # Your code here
        self.color = # Your code here
        
        # Set a fixed size for the enemy
        self.radius = 20

    def move(self):
        """
        Move the enemy across the screen
        TODO: Update the x-position by adding the speed
        Hint: Negative speed will move left
        """
        self.x += # Your code here

    def draw(self, screen):
        """
        Draw the enemy on the screen
        TODO: Use pygame.draw.circle to create the enemy
        """
        # Draw the enemy circle
        pygame.draw.circle(screen, # Your color parameter
                           (int(self.x), int(self.y)), # Position
                           # Your radius parameter
                           )

    def is_clicked(self, mouse_pos):
        """
        Check if the enemy was clicked
        TODO: Calculate the distance between mouse and enemy
        Hint: Use the distance formula: sqrt((x2-x1)²+(y2-y1)²)
        """
        # Calculate distance between mouse and enemy center
        dist = ((self.x - # mouse x
                 mouse_pos[0]) ** 2 + 
                (self.y - # mouse y
                 mouse_pos[1]) ** 2) ** 0.5
        
        # Check if distance is less than or equal to enemy radius
        return dist <= # Your comparison here

    def take_damage(self, damage):
        """
        Reduce enemy health when hit
        TODO: Subtract damage from health
        """
        self.health -= # Your code here
        return # Return how much damage was done

# Game Loop
# Create clock to control game speed
clock = pygame.time.Clock()

# Create a list to store enemies
enemies = []

# Game running flag
running = True

while running:
    # Fill screen with white each frame
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            running = False
        
        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            
            # Check each enemy if clicked
            enemies_to_remove = []
            for enemy in enemies:
                if enemy.is_clicked(mouse_pos):
                    # Destroy enemy if clicked
                    enemies_to_remove.append(enemy)
            
            # Remove clicked enemies
            for enemy in enemies_to_remove:
                enemies.remove(enemy)
    
    # Randomly spawn new enemies
    if random.randint(1, 30) == 1:
        new_enemy = Enemy(
            x=SCREEN_WIDTH,  # Start from right side
            y=random.randint(50, SCREEN_HEIGHT - 50),  # Random height
            health=50,  # Starting health
            speed=-2,   # Move left
            color=RED   # Enemy color
        )
        enemies.append(new_enemy)
    
    # Update and draw enemies
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
    
    # Remove enemies that go off screen
    enemies = [e for e in enemies if e.x > 0]
    
    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
