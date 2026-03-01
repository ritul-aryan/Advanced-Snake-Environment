# src/entities/apple.py
import random
import pygame
from src.settings import GRID_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, GOLDEN_APPLE_CHANCE, GOLDEN_APPLE_LIFETIME, GOLD

class Apple:
    def __init__(self, resource_manager):
        self.image = resource_manager.images.get('apple')
        self.x = 0
        self.y = 0
        self.is_golden = False
        self.golden_timer = 0
        self.randomize_position()

    def randomize_position(self, snake_body=[]):
        max_x = (WINDOW_WIDTH // GRID_SIZE) - 1
        max_y = (WINDOW_HEIGHT // GRID_SIZE) - 1
        
        while True:
            self.x = random.randint(0, max_x) * GRID_SIZE
            self.y = random.randint(0, max_y) * GRID_SIZE
            # Ensure it doesn't spawn inside the snake
            if not any(bx == self.x and by == self.y for bx, by in snake_body):
                break

        # Risk/Reward: Chance to become a golden apple
        if random.random() < GOLDEN_APPLE_CHANCE:
            self.is_golden = True
            self.golden_timer = GOLDEN_APPLE_LIFETIME
        else:
            self.is_golden = False

    def update(self):
        if self.is_golden:
            self.golden_timer -= 1
            if self.golden_timer <= 0:
                self.is_golden = False # Reverts to normal if you aren't fast enough!

    def draw(self, surface):
        if self.is_golden:
            # Draw a glowing aura behind it
            pygame.draw.circle(surface, GOLD, (self.x + GRID_SIZE//2, self.y + GRID_SIZE//2), GRID_SIZE//2 + 5)
        
        surface.blit(self.image, (self.x, self.y))