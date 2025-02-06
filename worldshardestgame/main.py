import pygame
from classes import Player, Coin, Wall, LineEnemy, RadialEnemy, Level

pygame.init()

# GAME VARIABLES
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
COIN_COLOR = (255, 215, 0)
WALL_COLOR = (255, 0, 0)
LINE_ENEMY_COLOR = (0, 0, 255)
RADIAL_ENEMY_COLOR = (255, 0, 255)
PLAYER_SIZE = 20
COIN_SIZE = 15
PLAYER_SPEED = 5

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player(x, y, size, color, speed)
player = Player(50, HEIGHT // 2, PLAYER_SIZE, PLAYER_COLOR, PLAYER_SPEED)
# Coin(x, y, size, color)
coin = Coin(WIDTH - 50, HEIGHT // 2, COIN_SIZE, COIN_COLOR)

# Creating outer walls
outer1 = Wall(0, 0, WIDTH, 20, WALL_COLOR)
outer2 = Wall(0, 0, 20, HEIGHT, WALL_COLOR)
outer3 = Wall(0, HEIGHT - 20, WIDTH, 20, WALL_COLOR)
outer4 = Wall(WIDTH - 20, 0, 20, HEIGHT, WALL_COLOR)
outers = [outer1, outer2, outer3, outer4]


# LEVEL 1: WALLS
# Wall(x, y, width, height, color)
wall_1 = Wall(200, 200, 400, 20, WALL_COLOR)
wall_2 = Wall(200, 200, 20, 200, WALL_COLOR)

# Level(walls, line_enemies, radial_enemies)
level1 = Level([wall_1] + outers, [], [])

# LEVEL 2: LINE ENEMIES
enemy_L1 = LineEnemy(300, 300, 500, 300, 2, LINE_ENEMY_COLOR)
enemy_L2 = LineEnemy(300, 500, 500, 500, 2, LINE_ENEMY_COLOR)
# Level(walls, line_enemies, radial_enemies)
level2 = Level([] + outers, [enemy_L1, enemy_L2], [])

# LEVEL 3: RADIAL ENEMIES
enemy_R1 = RadialEnemy(WIDTH // 2, HEIGHT // 2, 100, 0.01, RADIAL_ENEMY_COLOR)
enemy_R2 = RadialEnemy(WIDTH // 2, HEIGHT // 2, 200, 0.01, RADIAL_ENEMY_COLOR)
enemy_R3 = RadialEnemy(WIDTH // 2, HEIGHT // 2, 300, 0.01, RADIAL_ENEMY_COLOR)
level3 = Level([] + outers, [], [enemy_R1, enemy_R2, enemy_R3])

# LEVEL 4: WALLS, LINE ENEMIES, RADIAL ENEMIES
# Level(walls, line_enemies, radial_enemies)
level4 = Level([wall_1, wall_2] + outers, [enemy_L1, enemy_L2], [enemy_R1, enemy_R2, enemy_R3])

# ALL LEVELS
levels = [level1, level2, level3, level4]
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
