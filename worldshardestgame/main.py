import pygame
from classes import Player, Coin, Wall, LineEnemy, RadialEnemy, Level

# Initialize Pygame
pygame.init()

# COLORS = (RED, GREEN, BLUE)
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
COIN_COLOR = (255, 215, 0)
WALL_COLOR = (255, 0, 0)
LINE_ENEMY_COLOR = (0, 0, 255)
RADIAL_ENEMY_COLOR = (255, 0, 255)

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set Up Player
# Player(x, y, size, color, speed)
player = Player(50, 300, 20, PLAYER_COLOR, 5)

# Set Up Coin
# Coin(x, y, size, color)
coin = Coin(WIDTH - 50, 300, 15, COIN_COLOR)

# Creating outer walls
outer1 = Wall(0, 0, WIDTH, 20, WALL_COLOR)
outer2 = Wall(0, 0, 20, HEIGHT, WALL_COLOR)
outer3 = Wall(0, HEIGHT - 20, WIDTH, 20, WALL_COLOR)
outer4 = Wall(WIDTH - 20, 0, 20, HEIGHT, WALL_COLOR)
outers = [outer1, outer2, outer3, outer4]

# Defining Levels
# LEVEL 1: Just Outer Walls
# Level(walls, line_enemies, radial_enemies)
level1 = Level(outers, [], [])

# LEVEL 2: Add More Walls
# Wall(x, y, width, height, color)
wall_1 = Wall(350, 200, 100, 200, WALL_COLOR)
wall_2 = Wall(200, 0, 50, 400, WALL_COLOR)
# TODO: Make your own wall and add it
level2 = Level([wall_1, wall_2] + outers, [], [])

# LEVEL 3: Line Enemies!
# LineEnemy(x1, y1, x2, y2, speed, color)
enemy_L1 = LineEnemy(300, 300, 500, 300, 2, LINE_ENEMY_COLOR)
enemy_L2 = LineEnemy(300, 500, 500, 500, 2, LINE_ENEMY_COLOR)
# TODO: Make your own line enemy and add it
level3 = Level(outers, [enemy_L1, enemy_L2], [])

# LEVEL 4: Radial Enemies!
# RadialEnemy(cx, cy, radius, speed, color)
enemy_R1 = RadialEnemy(400, 300, 100, 0.01, RADIAL_ENEMY_COLOR)
enemy_R2 = RadialEnemy(400, 300, 200, 0.01, RADIAL_ENEMY_COLOR)
enemy_R3 = RadialEnemy(400, 300, 300, 0.01, RADIAL_ENEMY_COLOR)
# TODO: Make your own radial enemy and add it
level4 = Level(outers, [], [enemy_R1, enemy_R2, enemy_R3])

# LEVEL 5: Put the pieces together for the ULTIMATE LEVEL
level5 = Level([wall_1, wall_2] + outers, [enemy_L1, enemy_L2], [enemy_R1, enemy_R2, enemy_R3])

# CREATE YOUR OWN LEVELS NOW:
# Wall(x, y, width, height, color)
# LineEnemy(x1, y1, x2, y2, speed, color)
# RadialEnemy(cx, cy, radius, speed, color)
# Level(walls, line_enemies, radial_enemies)


# PUT ALL LEVELS HERE
levels = [level1, level2, level3, level4, level5]
level = 0

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    
    player.move(keys)
    
    # Check for coin collection
    if player.rect.colliderect(coin.rect):
        level += 1
        player.rect.x, player.rect.y = 50, HEIGHT // 2
        if level >= len(levels):
            level = 0
    
    # Check for collisions with enemies
    for enemy in levels[level].line_enemies + levels[level].radial_enemies:
        if player.rect.colliderect(enemy.rect):
            player.rect.x, player.rect.y = 50, HEIGHT // 2
    
    # Check for collisions with walls
    for wall in levels[level].walls:
        if player.rect.colliderect(wall.rect):
            player.rect.x, player.rect.y = 50, HEIGHT // 2
    
    levels[level].play(screen, player, coin)
    clock.tick(60)

pygame.quit()
