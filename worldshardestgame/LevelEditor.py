import pygame
import math

# Constants
BG_COLOR = (30, 30, 30)
WIDTH, HEIGHT = 800, 600
# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
COIN_COLOR = (255, 215, 0)
WALL_COLOR = (255, 0, 0)
LINE_ENEMY_COLOR = (0, 0, 255)
RADIAL_ENEMY_COLOR = (255, 0, 255)
PREVIEW_COLOR = (128, 128, 128, 128)  # Semi-transparent gray

class LevelEditor:
    def __init__(self):
        self.prints = 0
        self.walls = []
        self.line_enemies = []
        self.radial_enemies = []
        self.mode = None  # 1: Wall, 2: Radial Enemy, 3: Line Enemy
        self.line_start = None  # For line enemy first click
        self.preview_radius = 100  # For radial enemy preview
        self.preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.shift_pressed = False  # Track shift key state
        self.wall_width = 100  # Default wall width
        self.wall_height = 200  # Default wall height
        
    def handle_input(self):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        
        # Mode selection
        if keys[pygame.K_1]:
            self.mode = 1
        elif keys[pygame.K_2]:
            self.mode = 2
        elif keys[pygame.K_3]:
            self.mode = 3
            
        # Size adjustments based on mode
        if self.mode == 1:  # Wall mode
            if keys[pygame.K_LEFT]:
                self.wall_width = max(20, self.wall_width - 5)
            elif keys[pygame.K_RIGHT]:
                self.wall_width = min(400, self.wall_width + 5)
            if keys[pygame.K_DOWN]:
                self.wall_height = max(20, self.wall_height - 5)
            elif keys[pygame.K_UP]:
                self.wall_height = min(400, self.wall_height + 5)
        elif self.mode == 2:  # Radial enemy mode
            if keys[pygame.K_UP]:
                self.preview_radius = min(300, self.preview_radius + 5)
            elif keys[pygame.K_DOWN]:
                self.preview_radius = max(50, self.preview_radius - 5)
                
        # Show constructor when shift is newly pressed
        shift_now = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        if shift_now and not self.shift_pressed:
            self.prints += 1
            self.print_constructor()
        self.shift_pressed = shift_now
            
        return mouse_pos
    
    def draw_preview(self, mouse_pos):
        self.preview_surface.fill((0, 0, 0, 0))  # Clear with transparent
        
        if self.mode == 1:  # Wall preview
            pygame.draw.rect(self.preview_surface, PREVIEW_COLOR, 
                           pygame.Rect(mouse_pos[0] - self.wall_width//2, 
                                     mouse_pos[1] - self.wall_height//2, 
                                     self.wall_width, self.wall_height))
            
        elif self.mode == 2:  # Radial enemy preview
            pygame.draw.circle(self.preview_surface, PREVIEW_COLOR, 
                             mouse_pos, self.preview_radius)
            pygame.draw.rect(self.preview_surface, RADIAL_ENEMY_COLOR,
                           pygame.Rect(mouse_pos[0]-10, mouse_pos[1]-10, 20, 20))
            
        elif self.mode == 3 and self.line_start:  # Line enemy preview
            pygame.draw.line(self.preview_surface, PREVIEW_COLOR,
                           self.line_start, mouse_pos, 5)
            pygame.draw.rect(self.preview_surface, LINE_ENEMY_COLOR,
                           pygame.Rect(self.line_start[0]-10, self.line_start[1]-10, 20, 20))
    
    def handle_click(self, pos):
        if self.mode == 1:  # Wall
            wall = Wall(pos[0] - self.wall_width//2, 
                       pos[1] - self.wall_height//2, 
                       self.wall_width, self.wall_height, WALL_COLOR)
            self.walls.append(wall)
            
        elif self.mode == 2:  # Radial enemy
            enemy = RadialEnemy(pos[0], pos[1], self.preview_radius, 0.01, RADIAL_ENEMY_COLOR)
            self.radial_enemies.append(enemy)
            
        elif self.mode == 3:  # Line enemy
            if not self.line_start:
                self.line_start = pos
            else:
                enemy = LineEnemy(self.line_start[0], self.line_start[1], 
                                pos[0], pos[1], 2, LINE_ENEMY_COLOR)
                self.line_enemies.append(enemy)
                self.line_start = None
    
    def print_constructor(self):
        print("\n=== Level Constructor ===")
        # Print wall declarations
        print("#w_ = Wall(x, y, width, height, WALL_COLOR)")
        for i, wall in enumerate(self.walls, 1):
            print(f"w{i}_{self.prints} = Wall({wall.rect.x}, {wall.rect.y}, "
                  f"{wall.rect.width}, {wall.rect.height}, WALL_COLOR)")
        
        # Print line enemy declarations
        print("#l_{self.prints} = LineEnemy(x1, y1, x2, y2, speed, LINE_ENEMY_COLOR)")
        for i, enemy in enumerate(self.line_enemies, 1):
            print(f"l{i} = LineEnemy({enemy.start_x}, {enemy.start_y}, "
                  f"{enemy.end_x}, {enemy.end_y}, 2, LINE_ENEMY_COLOR)")
        
        # Print radial enemy declarations
        print("#r_{self.prints} = RadialEnemy(cx, cy, radius, speed, RADIAL_ENEMY_COLOR)")
        for i, enemy in enumerate(self.radial_enemies, 1):
            print(f"r{i} = RadialEnemy({enemy.cx}, {enemy.cy}, "
                  f"{enemy.radius}, 0.01, RADIAL_ENEMY_COLOR)")
        
        # Print level constructor
        wall_vars = [f"w{i}{self.prints}" for i in range(1, len(self.walls) + 1)]
        line_vars = [f"l{i}{self.prints}" for i in range(1, len(self.line_enemies) + 1)]
        rad_vars = [f"r{i}{self.prints}" for i in range(1, len(self.radial_enemies) + 1)]
        
        wall_str = f"[{', '.join(wall_vars)}]+outers" if wall_vars else "outers"
        line_str = f"[{', '.join(line_vars)}]" if line_vars else "[]"
        rad_str = f"[{', '.join(rad_vars)}]" if rad_vars else "[]"
        
        print(f"\nlevel_{self.prints} = Level({wall_str}, {line_str}, {rad_str})")
        print("==================")

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
        self.color = color
        self.direction = 1
        
        # Calculate movement increments
        dx = x2 - x1
        dy = y2 - y1
        distance = (dx**2 + dy**2) ** 0.5  # Euclidean distance
        self.norm_x = (dx / distance) * speed
        self.norm_y = (dy / distance) * speed

    def move(self):
        self.rect.x += self.norm_x * self.direction
        self.rect.y += self.norm_y * self.direction

        # Check if it reached the end or start point
        if self.direction == 1 and (self.rect.x >= self.end_x and self.rect.y >= self.end_y):
            self.direction = -1
        elif self.direction == -1 and (self.rect.x <= self.start_x and self.rect.y <= self.start_y):
            self.direction = 1

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
