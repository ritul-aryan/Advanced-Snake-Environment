# src/entities/particles.py
import pygame
import random

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit(self, x, y, color):
        # Create 10-15 particles at the given location
        for _ in range(random.randint(10, 15)):
            self.particles.append({
                'x': x + 20, # Center of the grid square
                'y': y + 20,
                'vx': random.uniform(-4, 4),
                'vy': random.uniform(-4, 4),
                'timer': random.randint(10, 20),
                'color': color
            })

    def update_and_draw(self, surface):
        for p in self.particles[:]:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['timer'] -= 1
            
            # Draw the particle (shrinks as timer goes down)
            size = max(1, p['timer'] // 3)
            pygame.draw.circle(surface, p['color'], (int(p['x']), int(p['y'])), size)
            
            if p['timer'] <= 0:
                self.particles.remove(p)