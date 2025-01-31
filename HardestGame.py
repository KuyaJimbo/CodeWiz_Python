import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
OBSTACLE_RADIUS = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = 3

    def move(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        # add movement to the left with pygame.K_a
        
        # add movement to the right with pygame.K_d

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

class Obstacle:
    def __init__(self, x, y, vert_range=0, vert_timer=0, horiz_range=0, horiz_timer=0):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.vert_range = vert_range
        self.vert_timer = vert_timer
        self.horiz_range = horiz_range
        self.horiz_timer = horiz_timer
        self.time = 0

    def update(self):
        self.time += 1
        if self.vert_range:
            self.y = self.start_y + self.vert_range * math.sin(self.time / self.vert_timer * 2 * math.pi)
        if self.horiz_range:
            self.x = self.start_x + self.horiz_range * math.cos(self.time / self.horiz_timer * 2 * math.pi)

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), OBSTACLE_RADIUS)
    
    def collides_with(self, player):
        return pygame.Rect(self.x - OBSTACLE_RADIUS, self.y - OBSTACLE_RADIUS, OBSTACLE_RADIUS * 2, OBSTACLE_RADIUS * 2).colliderect(player.rect)

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)
    
    def collides_with(self, player):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2).colliderect(player.rect)

class Level:
    def __init__(self, player_start, obstacles_info, coin_pos):
        self.player = Player(*player_start)
        self.obstacles = [Obstacle(*info) for info in obstacles_info]
        self.coin = Coin(*coin_pos)

    def update(self, keys):
        self.player.move(keys)
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.collides_with(self.player):
                print("Game Over!")
                pygame.quit()
                exit()
        
        if self.coin.collides_with(self.player):
            return True  # Move to next level
        return False

    def draw(self, screen):
        self.player.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.coin.draw(screen)

# Define levels
levels = [
    Level((200, 200), [(250, 250, 120, 90, 120, 90)], (600, 400)),

    Level(
      (100, 100), 
      [(200, 200, 100, 120, 0, 0),
       (400, 300, 0, 0, 150, 180)
      ],
      (700, 500)
    ),
    
    Level(
      (50, 50),
      [(300, 200, 0, 0, 150, 100), 
       (500, 400, 0, 0, 200, 150)
      ],
      (750, 550)
    )
    
    
]

current_level = 0
running = True
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if levels[current_level].update(keys):
        current_level += 1
        if current_level >= len(levels):
            print("You Win!")
            running = False
    
    levels[current_level].draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
