import pygame, math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
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

# Classes
class Player:
    def __init__(self, x, y, size, color, speed):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = speed
    
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Coin:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

class Wall:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class LineEnemy:
    def __init__(self, x1, y1, x2, y2, speed, color):
        self.rect = pygame.Rect(x1, y1, 20, 20)
        self.start_x, self.start_y = x1, y1
        self.end_x, self.end_y = x2, y2
        self.speed = speed
        self.direction = 1
        self.color = color
    
    def move(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x >= self.end_x or self.rect.x <= self.start_x:
            self.direction *= -1
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class RadialEnemy:
    def __init__(self, cx, cy, radius, speed, color):
        self.cx, self.cy = cx, cy
        self.radius = radius
        self.angle = 0
        self.speed = speed
        self.color = color
    
    def move(self):
        self.angle += self.speed
        x = self.cx + self.radius * math.cos(self.angle)
        y = self.cy + self.radius * math.sin(self.angle)
        self.rect = pygame.Rect(x, y, 20, 20)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Level:
    def __init__(self, walls, line_enemies, radial_enemies):
        self.walls = walls
        self.line_enemies = line_enemies
        self.radial_enemies = radial_enemies
    
    def play(self, player, coin):
        screen.fill(BG_COLOR)
        player.draw(screen)
        coin.draw(screen)
        
        for wall in self.walls:
            wall.draw(screen)
        for enemy in self.line_enemies:
            enemy.move()
            enemy.draw(screen)
        for enemy in self.radial_enemies:
            enemy.move()
            enemy.draw(screen)
        
        pygame.display.flip()

# Initialize levels
player = Player(50, HEIGHT // 2, PLAYER_SIZE, PLAYER_COLOR, PLAYER_SPEED)
coin = Coin(WIDTH - 50, HEIGHT // 2, COIN_SIZE, COIN_COLOR)
walls = [Wall(200, 200, 50, 300, WALL_COLOR)]
line_enemies = [LineEnemy(300, 300, 500, 300, 2, LINE_ENEMY_COLOR)]
radial_enemies = [RadialEnemy(600, 400, 50, 0.05, RADIAL_ENEMY_COLOR)]

levels = [Level(walls, line_enemies, radial_enemies) for _ in range(3)]
level = 0

# Game loop
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.move(keys)
    
    if player.rect.colliderect(coin.rect):
        level += 1
        player.rect.x, player.rect.y = 50, HEIGHT // 2
        if level >= len(levels):
            level = 0
    
    for enemy in levels[level].line_enemies:
        if player.rect.colliderect(enemy.rect):
            player.rect.x, player.rect.y = 50, HEIGHT // 2
    
    for wall in levels[level].walls:
        if player.rect.colliderect(wall.rect):
            player.rect.x, player.rect.y = 50, HEIGHT // 2
    
    levels[level].play(player, coin)
    clock.tick(60)

pygame.quit()
