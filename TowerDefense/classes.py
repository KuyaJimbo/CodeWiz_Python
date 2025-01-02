import pygame
import random

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class GameState:
    def __init__(self):
        self.score = 0
        self.game_over = False

class Enemy:
    def __init__(self, x, y, health, speed, color):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.speed = speed
        self.color = color
        self.radius = 20

    def move(self):
        self.x += self.speed

    def draw(self, screen):
        # Draw enemy
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw health bar
        health_width = self.radius * 2
        health_height = 5
        health_bar_x = int(self.x - health_width / 2)
        health_bar_y = int(self.y - self.radius - 10)
        
        # Background of health bar
        pygame.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_width, health_height))
        
        # Current health of health bar
        current_health_width = int(health_width * (self.health / self.max_health))
        pygame.draw.rect(screen, GREEN, (health_bar_x, health_bar_y, current_health_width, health_height))

    def is_clicked(self, mouse_pos):
        dist = ((self.x - mouse_pos[0]) ** 2 + (self.y - mouse_pos[1]) ** 2) ** 0.5
        return dist <= self.radius

    def take_damage(self, damage):
        self.health -= damage
        return damage  # Return damage for scoring

class Tower:
    def __init__(self, x, y, cost, health, damage, fire_rate):
        self.x = x
        self.y = y
        self.cost = cost
        self.health = health
        self.max_health = health
        self.damage = damage
        self.fire_rate = fire_rate
        self.fire_cooldown = 0
        self.size = 40

    def draw(self, screen):
        if self.damage == 20:   # basic towers are light blue
            pygame.draw.rect(screen, (0, 0, 100), (self.x, self.y, self.size, self.size))
        else:   # strong towers are dark blue
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))
        
        # Draw health bar
        health_width = self.size
        health_height = 5
        health_bar_x = self.x
        health_bar_y = self.y - 10
        
        # Background of health bar
        pygame.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_width, health_height))
        
        # Current health of health bar
        current_health_width = int(health_width * (self.health / self.max_health))
        pygame.draw.rect(screen, GREEN, (health_bar_x, health_bar_y, current_health_width, health_height))

    def is_hovered(self, mouse_pos):
        mx, my = mouse_pos
        return self.x <= mx <= self.x + self.size and self.y <= my <= self.y + self.size

    def take_damage(self, damage):
        self.health -= damage
        return damage