import pygame

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Cookie Class
class Cookie:
    def __init__(self, x, y, radius, value, color):
        # create cookie's x, y, radius, and value
        self.x, self.y, self.radius, self.value = x, y, radius, value
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (400, 300), 100)

    def clicked(self, pos):
        return ((pos[0] - self.x)**2 + (pos[1] - self.y)**2)**0.5 <= self.radius

# Create the cookie object: Cookie(x, y, radius, value, color)
cookie = Cookie(400, 300, 100, 1, BROWN)

# Upgrade Class
class Upgrade:
    # What does an upgrade need?
    def __init__(self, x, y, width, height, name, price, value, quantity, color):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.name, self.price, self.value = name, price, value
        self.quantity, self.color = quantity, color

    def draw(self):
        pygame.draw.rect(screen, self.color,
                    (self.x, self.y, self.width, self.height))
        screen.blit(font.render(f"{self.name}: {self.quantity}", True, BLACK),
                    (self.x + 10, self.y + 10))
        screen.blit(font.render(f"Price: {self.price}", True, BLACK),
                    (self.x + 10, self.y + 40))
        screen.blit(font.render(f"Value: {self.value}/s", True, BLACK),
                    (self.x + 10, self.y + 70))

    def clicked(self, pos): 
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[
            1] <= self.y + self.height

# Create an upgrade object: Upgrade(x, y, width, height, name, price, value)
auto_clicker = Upgrade(600, 100, 150, 100, "AUTO", 15, 1, 0, LIGHT_GRAY)
factory =      Upgrade(600, 250, 150, 100, "FACTORY", 20, 5, 0, LIGHT_GRAY)

upgrade_list = [auto_clicker, factory]

# Game Variables
total_cookies = 0
cookies_per_second = 0
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if cookie.clicked(event.pos):
                total_cookies += 1
                
            for upgrade in upgrade_list:
                if upgrade.clicked(event.pos):
                    if total_cookies >= upgrade.price:
                        total_cookies -= upgrade.price              # Subtract price from total cookies
                        upgrade.quantity += 1                       # Increase quantity of cookies
                        upgrade.price = int(upgrade.price * 1.5)    # Increase the price
                        cookies_per_second += upgrade.value         # Increase cookies per second

    # Draw the background first
    screen.fill(WHITE)

    # Draw the game objects
    cookie.draw()
    auto_clicker.draw()
    factory.draw()
    
    # Draw the Score
    screen.blit(font.render(f"Cookies: {int(total_cookies)}", True, BLACK),
                (10, 10))
    screen.blit(font.render(f"Per second: {cookies_per_second}", True, BLACK),
                (10, 50))
    
    # Add cookies per second
    total_cookies += cookies_per_second / 60
    
    # Update the screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS (Frames Per Second)
