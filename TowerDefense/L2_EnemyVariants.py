import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense: Enemy Variants")

# Color Palette - More Variety!
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Enemy Class with More Customization
class Enemy:
    def __init__(self, x, y, health, speed, color, enemy_type):
        """
        Create an advanced enemy with more characteristics
        
        Parameters:
        - x: Starting x-position
        - y: Starting y-position
        - health: How many hits it can take
        - speed: How fast it moves
        - color: What color the enemy appears
        - enemy_type: Special characteristics of the enemy
        """
        # Core enemy attributes
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health  # Remember original health
        self.speed = speed
        self.color = color
        self.radius = 20
        
        # New enemy type system
        self.enemy_type = enemy_type
        
        # Special abilities based on enemy type
        self.special_ability = self.get_special_ability()

    def get_special_ability(self):
        """
        Assign special abilities based on enemy type
        
        Types of enemies:
        1. 'standard': Normal enemy
        2. 'tank': High health
        3. 'speedy': Fast movement
        4. 'regenerating': Slowly regains health
        """
        abilities = {
            'standard': None,
            'tank': 2,  # Damage reduction multiplier
            'speedy': 1.5,  # Speed multiplier
            'regenerating': 1  # Health regeneration per frame
        }
        return abilities.get(self.enemy_type, None)

    def move(self):
        """
        Enhanced movement with type-based speed modification
        """
        # Apply speed boost for speedy enemies
        if self.enemy_type == 'speedy':
            self.x += self.speed * self.special_ability
        else:
            self.x += self.speed

    def take_damage(self, damage):
        """
        Advanced damage system with type-based modifications
        """
        # Damage reduction for tank enemies
        if self.enemy_type == 'tank':
            damage = max(1, damage // self.special_ability)
        
        # Reduce health
        self.health -= damage
        
        # Regenerate health for regenerating enemies
        if self.enemy_type == 'regenerating':
            self.health = min(self.max_health, self.health + self.special_ability)
        
        return damage

    def draw(self, screen):
        """
        Draw enemy with health bar and type-based appearance
        """
        # Choose drawing style based on enemy type
        if self.enemy_type == 'tank':
            # Thicker border for tank enemies
            pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius + 2)
        
        # Draw main enemy circle
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Health bar
        health_width = self.radius * 2
        health_height = 5
        health_bar_x = int(self.x - health_width / 2)
        health_bar_y = int(self.y - self.radius - 10)
        
        # Background of health bar (red)
        pygame.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_width, health_height))
        
        # Current health of health bar (green)
        current_health_width = int(health_width * (self.health / self.max_health))
        pygame.draw.rect(screen, GREEN, (health_bar_x, health_bar_y, current_health_width, health_height))

    def is_clicked(self, mouse_pos):
        """
        Check if the enemy was clicked
        """
        dist = ((self.x - mouse_pos[0]) ** 2 + (self.y - mouse_pos[1]) ** 2) ** 0.5
        return dist <= self.radius

# Game Loop with Enemy Variety
clock = pygame.time.Clock()
enemies = []
running = True

# Enemy type probabilities
enemy_types = [
    {'type': 'standard', 'health': 50, 'speed': -2, 'color': RED},
    {'type': 'tank', 'health': 100, 'speed': -1, 'color': BLUE},
    {'type': 'speedy', 'health': 25, 'speed': -3, 'color': GREEN},
    {'type': 'regenerating', 'health': 75, 'speed': -1.5, 'color': PURPLE}
]

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            enemies_to_remove = []
            
            for enemy in enemies:
                if enemy.is_clicked(mouse_pos):
                    enemies_to_remove.append(enemy)
            
            for enemy in enemies_to_remove:
                enemies.remove(enemy)
    
    # Spawn new enemies with variety
    if random.randint(1, 30) == 1:
        enemy_config = random.choice(enemy_types)
        new_enemy = Enemy(
            x=SCREEN_WIDTH,
            y=random.randint(50, SCREEN_HEIGHT - 50),
            health=enemy_config['health'],
            speed=enemy_config['speed'],
            color=enemy_config['color'],
            enemy_type=enemy_config['type']
        )
        enemies.append(new_enemy)
    
    # Update and draw enemies
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
    
    # Remove off-screen enemies
    enemies = [e for e in enemies if e.x > 0]
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
