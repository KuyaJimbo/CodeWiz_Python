# LEVEL DESIGNER
import pygame
from classes import Player, Coin, Wall, LineEnemy, RadialEnemy, Level, BG_COLOR, LevelEditor

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
COIN_COLOR = (255, 215, 0)
WALL_COLOR = (255, 0, 0)
LINE_ENEMY_COLOR = (0, 0, 255)
RADIAL_ENEMY_COLOR = (255, 0, 255)
PREVIEW_COLOR = (128, 128, 128, 128)  # Semi-transparent gray

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create outer walls
outer1 = Wall(0, 0, WIDTH, 20, WALL_COLOR)
outer2 = Wall(0, 0, 20, HEIGHT, WALL_COLOR)
outer3 = Wall(0, HEIGHT - 20, WIDTH, 20, WALL_COLOR)
outer4 = Wall(WIDTH - 20, 0, 20, HEIGHT, WALL_COLOR)
outers = [outer1, outer2, outer3, outer4]

editor = LevelEditor()
running = True

while running:
    mouse_pos = editor.handle_input()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            editor.handle_click(mouse_pos)
    
    # Draw
    screen.fill(BG_COLOR)
    
    # Draw outer walls
    for wall in outers:
        wall.draw(screen)
    
    # Draw placed objects
    for wall in editor.walls:
        wall.draw(screen)
    for enemy in editor.line_enemies:
        enemy.draw(screen)
    for enemy in editor.radial_enemies:
        enemy.draw(screen)
    
    # Draw preview
    editor.draw_preview(mouse_pos)
    screen.blit(editor.preview_surface, (0, 0))
    
    pygame.display.flip()
    clock.tick(60)
