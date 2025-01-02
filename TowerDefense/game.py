import pygame
import random
import sys
from classes import GameState, Enemy, Tower

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
MENU_WIDTH = 150
PLAY_AREA_WIDTH = WIDTH - MENU_WIDTH

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game font
font = pygame.font.Font(None, 36)

# Initialize game state
game_state = GameState()

# Side menu buttons for towers
buttons = [
    {"type": "basic_tower", "cost": 50, "tower": Tower(50, 100, 50, 100, 10, 1)},
    {"type": "strong_tower", "cost": 100, "tower": Tower(50, 250, 100, 200, 20, 0.5)},
]

# Game loop variables
enemies = []
towers = []
held_tower = None

def spawn_enemy():
    """Randomly generate a new enemy."""
    enemy_types = [
        {"health": 50, "speed": 1, "color": (200, 0, 0)},    # Weak enemy
        {"health": 100, "speed": 0.5, "color": (150, 0, 0)}, # Strong enemy
        {"health": 25, "speed": 2, "color": (250, 0, 0)},    # Fast enemy
    ]
    enemy_type = random.choice(enemy_types)
    new_enemy = Enemy(
        x=WIDTH - MENU_WIDTH,  # Start on the right side of the screen
        y=random.randint(50, HEIGHT - 50),
        health=enemy_type["health"],
        speed=-enemy_type["speed"],  # Negative speed to move left
        color=enemy_type["color"]
    )
    enemies.append(new_enemy)

running = True

while running:
    screen.fill(WHITE)

    # Draw side menu
    pygame.draw.rect(screen, GRAY, (0, 0, MENU_WIDTH, HEIGHT))

    # Render score
    score_text = font.render(f"Score: {game_state.score}", True, BLACK)
    screen.blit(score_text, (10, HEIGHT - 50))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Check for clicking enemies
            enemies_to_remove = []
            for enemy in enemies:
                if enemy.is_clicked(mouse_pos):
                    points_earned = enemy.health
                    game_state.score += points_earned
                    enemies_to_remove.append(enemy)
            
            # Remove clicked enemies
            for enemy in enemies_to_remove:
                enemies.remove(enemy)

            # Check if clicked in menu
            if mouse_pos[0] <= MENU_WIDTH:
                for button in buttons:
                    if button["tower"].is_hovered(mouse_pos):
                        # Check if player has enough points
                        if game_state.score >= button["cost"]:
                            # Create a new tower to hold
                            held_tower = Tower(
                                mouse_pos[0], 
                                mouse_pos[1], 
                                button["cost"], 
                                button["tower"].health, 
                                button["tower"].damage, 
                                button["tower"].fire_rate
                            )
                            held_tower.is_held = True
                            break

        elif event.type == pygame.MOUSEBUTTONUP:
            if held_tower:
                # Check if placed in the play area
                if held_tower.x > MENU_WIDTH and 0 <= held_tower.x < WIDTH and 0 <= held_tower.y < HEIGHT:
                    # Deduct cost of tower
                    game_state.score -= held_tower.cost
                    held_tower.is_held = False
                    towers.append(held_tower)
                # Otherwise, discard the tower
                held_tower = None

    # Update held tower position
    if held_tower:
        mouse_pos = pygame.mouse.get_pos()
        held_tower.x = mouse_pos[0] - 20  # Center adjustment
        held_tower.y = mouse_pos[1] - 20

    # Add new enemies periodically
    if random.randint(1, 30) == 1:
        spawn_enemy()

    # Update enemies
    enemies_to_remove = []
    for enemy in enemies:
        enemy.move()
        
        # Check for enemy reaching menu area
        if enemy.x < MENU_WIDTH:
            # Subtract points based on enemy's initial health
            game_state.score -= enemy.max_health
            enemies_to_remove.append(enemy)
        
        # Check collision with towers
        for tower in towers:
            if (abs(enemy.x - tower.x) < enemy.radius + tower.size and 
                abs(enemy.y - tower.y) < enemy.radius + tower.size):
                # Damage tower and enemy
                enemy_damage = enemy.take_damage(5)
                tower_damage = tower.take_damage(5)
                
                # Add damage to score
                game_state.score += tower_damage
                
                # Remove if health reaches 0
                if enemy.health <= 0:
                    enemies_to_remove.append(enemy)
                    game_state.score += enemy.max_health
                
                if tower.health <= 0:
                    towers.remove(tower)

    # Remove enemies that are off screen or destroyed
    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)

    # Update and draw towers
    for tower in towers:
        tower.draw(screen)

    # Update and draw enemies
    for enemy in enemies:
        enemy.draw(screen)

    # Draw menu buttons
    for button in buttons:
        button["tower"].draw(screen)
        # create ui text displaying cost of tower and health
        cost_text = font.render(f"Cost: {button['cost']}", True, BLACK)
        screen.blit(cost_text, (10, button["tower"].y + 50))
        health_text = font.render(f"Health: {button['tower'].health}", True, BLACK)
        screen.blit(health_text, (10, button["tower"].y + 70))

    # Draw held tower
    if held_tower:
        held_tower.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()