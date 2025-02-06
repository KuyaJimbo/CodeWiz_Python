import pygame
import math

# Constants
BG_COLOR = (30, 30, 30)

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
        self.rect = pygame.Rect(cx + radius, cy, 20, 20)
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
    
    def play(self, screen, player, coin):
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
