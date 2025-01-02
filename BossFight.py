import pygame
import random

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# TODO: Create a Bullet class with the following features:
# 1. Initialize the bullet with:
#    - x, y position (where the bullet spawns)
#    - width and height for the bullet rectangle
#    - speed (how fast the bullet moves)
#    - direction (1 for right, -1 for left)
#    - color (BLUE for player bullets, RED for boss bullets)
# 2. Create a pygame Rect for the bullet in __init__
# 3. Add a move method to update bullet position based on speed and direction
# 4. Add a draw method to draw the bullet on the screen
# Example structure:
"""
class Bullet:
    def __init__(self, x, y, width, height, speed, direction, color):
        # Initialize bullet properties here
    
    def move(self):
        # Update bullet position here
    
    def draw(self):
        # Draw bullet on screen here
"""


class Player:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = 50  # Spawn near left side
        self.y = HEIGHT // 2 - height // 2  # Vertical middle
        self.rect = pygame.Rect(self.x, self.y, width, height)
        # TODO: Add an empty bullets list to store player bullets
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y < HEIGHT - self.height:
            self.y += self.speed
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_d] and self.x < WIDTH - self.width:
            self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
    
    # TODO: Add shoot method that:
    # 1. Creates a new blue bullet at the player's position
    # 2. Sets bullet direction to 1 (right)
    # 3. Adds bullet to the player's bullets list
    
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Boss:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = WIDTH - width - 50  # Spawn near right side
        self.y = HEIGHT // 2 - height // 2  # Vertical middle
        self.rect = pygame.Rect(self.x, self.y, width, height)
        # TODO: Add an empty bullets list to store boss bullets
        self.health = 100
        self.move_counter = 0
        self.move_direction = 1
    
    def move(self):
        self.move_counter += 1
        if self.move_counter >= 60:  # Change direction every 60 frames
            self.move_direction = random.choice([-1, 1])
            self.move_counter = 0
        
        new_y = self.y + (self.speed * self.move_direction)
        if 0 <= new_y <= HEIGHT - self.height:
            self.y = new_y
        else:
            self.move_direction *= -1  # Reverse direction if hitting screen bounds
        
        self.rect.y = self.y
    
    # TODO: Add shoot method that:
    # 1. Uses random.random() to give a 2% chance to shoot
    # 2. Creates a new red bullet at the boss's position
    # 3. Sets bullet direction to -1 (left)
    # 4. Adds bullet to the boss's bullets list
    
    def hit(self):
        self.health -= 10
        return self.health <= 0
    
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
    
    def draw_health(self):
        health_rect = pygame.Rect(WIDTH//4, 20, WIDTH//2, 20)
        pygame.draw.rect(screen, RED, health_rect)
        current_health_rect = pygame.Rect(WIDTH//4, 20, 
                                        (WIDTH//2) * (self.health/100), 20)
        pygame.draw.rect(screen, GREEN, current_health_rect)

# Game Objects
player = Player(40, 60, 5)
boss = Boss(60, 80, 4)

# Game Variables
SCORE = 0

clock = pygame.time.Clock()

# Game Loop
while True:
    # Get Pygame Actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # TODO: Add event check for KEYDOWN
        # If SPACE key is pressed, call player.shoot()
    
    # Do Object Actions
    player.move()
    boss.move()
    # TODO: Call boss.shoot() here
    
    # TODO: Update and check player bullets:
    # 1. Loop through player.bullets[:] (use slice to avoid modification issues)
    # 2. Move each bullet
    # 3. Remove bullets that go off screen (x > WIDTH)
    # 4. Check collision with boss (bullet.rect.colliderect(boss.rect))
    # 5. If collision occurs:
    #    - Remove the bullet
    #    - Call boss.hit()
    #    - If boss is defeated (hit() returns True):
    #      * Add 100 to SCORE
    #      * Reset boss health to 100
    
    # TODO: Update and check boss bullets:
    # 1. Loop through boss.bullets[:] (use slice to avoid modification issues)
    # 2. Move each bullet
    # 3. Remove bullets that go off screen (x < 0)
    # 4. Check collision with player (bullet.rect.colliderect(player.rect))
    # 5. If collision occurs:
    #    - Remove the bullet
    #    - Subtract 10 from SCORE
    
    # Background Color
    screen.fill(BLACK)
    
    # Draw Game Objects
    player.draw()
    boss.draw()
    boss.draw_health()
    
    # TODO: Draw all bullets:
    # 1. Loop through and draw player.bullets
    # 2. Loop through and draw boss.bullets
    
    # Draw the Score
    screen.blit(font.render(f"SCORE: {int(SCORE)}", True, WHITE), (10, 10))
    
    # Update the screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS (Frames Per Second)
