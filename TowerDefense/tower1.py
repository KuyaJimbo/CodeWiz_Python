import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
MENU_WIDTH = 150
PLAY_AREA_WIDTH = WIDTH - MENU_WIDTH

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Balls and Shape Placement Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60


# Falling Ball Class
class FallingBall:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, mouse_pos):
        dist = ((self.x - mouse_pos[0]) ** 2 + (self.y - mouse_pos[1]) ** 2) ** 0.5
        return dist <= self.radius


# Base Shape Class
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_held = False

    def draw(self, screen):
        pass

    def is_hovered(self, mouse_pos):
        pass


class Square(Shape):
    def __init__(self, x, y, size=40):
        super().__init__(x, y)
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.size, self.size))

    def is_hovered(self, mouse_pos):
        mx, my = mouse_pos
        return self.x <= mx <= self.x + self.size and self.y <= my <= self.y + self.size


class Triangle(Shape):
    def __init__(self, x, y, size=40):
        super().__init__(x, y)
        self.size = size

    def draw(self, screen):
        points = [
            (self.x, self.y + self.size),
            (self.x + self.size // 2, self.y),
            (self.x + self.size, self.y + self.size),
        ]
        pygame.draw.polygon(screen, BLACK, points)

    def is_hovered(self, mouse_pos):
        mx, my = mouse_pos
        return self.x <= mx <= self.x + self.size and self.y <= my <= self.y + self.size


class Hexagon(Shape):
    def __init__(self, x, y, size=40):
        super().__init__(x, y)
        self.size = size

    def draw(self, screen):
        points = [
            (self.x + self.size // 2, self.y),
            (self.x + self.size, self.y + self.size // 3),
            (self.x + self.size, self.y + 2 * self.size // 3),
            (self.x + self.size // 2, self.y + self.size),
            (self.x, self.y + 2 * self.size // 3),
            (self.x, self.y + self.size // 3),
        ]
        pygame.draw.polygon(screen, BLACK, points)

    def is_hovered(self, mouse_pos):
        mx, my = mouse_pos
        return self.x <= mx <= self.x + self.size and self.y <= my <= self.y + self.size


# Side menu buttons
buttons = [
    {"shape": "square", "instance": Square(50, 50)},
    {"shape": "triangle", "instance": Triangle(50, 150)},
    {"shape": "hexagon", "instance": Hexagon(50, 250)},
]

# Game loop variables
falling_balls = []  # Active falling balls
shapes = []  # Placed shapes
held_shape = None


def spawn_ball():
    """Randomly generate a new falling ball."""
    new_ball = FallingBall(
        x=random.randint(MENU_WIDTH + 20, WIDTH - 20),
        y=0,
        radius=random.randint(15, 30),
        color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        speed=random.randint(2, 5),
    )
    falling_balls.append(new_ball)

running = True

while running:
    screen.fill(WHITE)

    # Draw side menu
    pygame.draw.rect(screen, GRAY, (0, 0, MENU_WIDTH, HEIGHT))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] <= MENU_WIDTH:  # Check if clicked in menu
                for button in buttons:
                    if button["instance"].is_hovered(mouse_pos):
                        # Create a new shape to hold
                        if button["shape"] == "square":
                            held_shape = Square(mouse_pos[0], mouse_pos[1])
                        elif button["shape"] == "triangle":
                            held_shape = Triangle(mouse_pos[0], mouse_pos[1])
                        elif button["shape"] == "hexagon":
                            held_shape = Hexagon(mouse_pos[0], mouse_pos[1])
                        held_shape.is_held = True
                        break
            else:
                # Check if clicked a falling ball
                balls_to_remove = [ball for ball in falling_balls if ball.is_clicked(mouse_pos)]
                for ball in balls_to_remove:
                    falling_balls.remove(ball)
        elif event.type == pygame.MOUSEBUTTONUP:
            if held_shape:
                # Check if placed in the play area
                if held_shape.x > MENU_WIDTH and 0 <= held_shape.x < WIDTH and 0 <= held_shape.y < HEIGHT:
                    held_shape.is_held = False
                    shapes.append(held_shape)
                # Otherwise, discard the shape
                held_shape = None

    # Update held shape position
    if held_shape and held_shape.is_held:
        mouse_pos = pygame.mouse.get_pos()
        held_shape.x = mouse_pos[0] - 20  # Center adjustment
        held_shape.y = mouse_pos[1] - 20

    # Add new falling balls periodically
    if random.randint(1, 20) == 1:
        spawn_ball()

    # Update and draw falling balls
    for ball in falling_balls:
        ball.move()
        ball.draw(screen)

    # Remove balls that fall off the screen
    falling_balls[:] = [ball for ball in falling_balls if ball.y - ball.radius < HEIGHT]

    # Draw menu buttons
    for button in buttons:
        button["instance"].draw(screen)

    # Draw placed shapes
    for shape in shapes:
        shape.draw(screen)

    # Draw held shape
    if held_shape:
        held_shape.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
