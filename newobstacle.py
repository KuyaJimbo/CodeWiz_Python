import pygame

class Obstacle:
    def __init__(self, x, y, vert_range=0, vert_speed=1, horiz_range=0, horiz_speed=1):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.vert_range = vert_range
        self.horiz_range = horiz_range
        self.vert_speed = vert_speed if vert_range else 0
        self.horiz_speed = horiz_speed if horiz_range else 0
        self.direction_x = 1  # 1 for forward, -1 for backward
        self.direction_y = 1  # 1 for downward, -1 for upward

    def update(self):
        # Horizontal movement
        if self.horiz_range:
            self.x += self.horiz_speed * self.direction_x
            if abs(self.x - self.start_x) >= self.horiz_range:
                self.direction_x *= -1  # Reverse direction

        # Vertical movement
        if self.vert_range:
            self.y += self.vert_speed * self.direction_y
            if abs(self.y - self.start_y) >= self.vert_range:
                self.direction_y *= -1  # Reverse direction

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), OBSTACLE_RADIUS)

    def collides_with(self, player):
        return pygame.Rect(self.x - OBSTACLE_RADIUS, self.y - OBSTACLE_RADIUS, OBSTACLE_RADIUS * 2, OBSTACLE_RADIUS * 2).colliderect(player.rect)
