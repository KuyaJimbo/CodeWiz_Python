import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Shape classes
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, controls, speed):
        if controls == "arrows":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= speed
            if keys[pygame.K_RIGHT]:
                self.x += speed
            if keys[pygame.K_UP]:
                self.y -= speed
            if keys[pygame.K_DOWN]:
                self.y += speed
        elif controls == "wasd":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.x -= speed
            if keys[pygame.K_d]:
                self.x += speed
            if keys[pygame.K_w]:
                self.y -= speed
            if keys[pygame.K_s]:
                self.y += speed

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self, controls, speed):
        if controls == "arrows":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= speed
            if keys[pygame.K_RIGHT]:
                self.x += speed
            if keys[pygame.K_UP]:
                self.y -= speed
            if keys[pygame.K_DOWN]:
                self.y += speed
        elif controls == "wasd":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.x -= speed
            if keys[pygame.K_d]:
                self.x += speed
            if keys[pygame.K_w]:
                self.y -= speed
            if keys[pygame.K_s]:
                self.y += speed

class Triangle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
    def draw(self, screen):
        point1 = (self.x, self.y - self.size // 2)
        point2 = (self.x - self.size // 2, self.y + self.size // 2)
        point3 = (self.x + self.size // 2, self.y + self.size // 2)
        pygame.draw.polygon(screen, self.color, [point1, point2, point3])
        
    def move(self, controls, speed):
        if controls == "arrows":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= speed
            if keys[pygame.K_RIGHT]:
                self.x += speed
            if keys[pygame.K_UP]:
                self.y -= speed
            if keys[pygame.K_DOWN]:
                self.y += speed
        elif controls == "wasd":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.x -= speed
            if keys[pygame.K_d]:
                self.x += speed
            if keys[pygame.K_w]:
                self.y -= speed
            if keys[pygame.K_s]:
                self.y += speed
# Create shapes
# Circle(x, y, radius, color)
circle = Circle(200, 300, 50, RED)
# Rectangle(x, y, width, height, color)
rectangle = Rectangle(400, 250, 100, 150, GREEN)
# Triangle(x, y, size, color)
triangle = Triangle(600, 350, 80. BLUE)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw shapes
    circle.draw(screen)
    rectangle.draw(screen)
    triangle.draw(screen)
    
    pygame.display.flip()

pygame.quit()
