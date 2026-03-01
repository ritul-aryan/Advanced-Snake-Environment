# src/core/playing_state.py
import pygame
import random
from src.core.state_machine import State
from src.entities.snake import Snake
from src.entities.apple import Apple
from src.entities.particles import ParticleSystem
from src.settings import GRID_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, FPS

class PlayingState(State):
    def __init__(self, engine, resource_manager):
        super().__init__(engine)
        self.resource_manager = resource_manager
        self.bg_image = self.resource_manager.images.get('background')
        self.font = pygame.font.SysFont('arial', 30, bold=True)
        self.particles = ParticleSystem()
        self.reset_game()

    def reset_game(self):
        self.snake = Snake(self.resource_manager)
        self.apple = Apple(self.resource_manager)
        self.score = 0
        self.current_speed = FPS
        self.engine.clock = pygame.time.Clock()
        self.paused = False
        self.shake_frames = 0
        self.particles.particles.clear()

    def is_collision(self, x1, y1, x2, y2):
        return x1 >= x2 and x1 < x2 + GRID_SIZE and y1 >= y2 and y1 < y2 + GRID_SIZE

    def trigger_crash(self):
        self.resource_manager.play_sound('crash')
        self.shake_frames = 12 

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                    self.paused = not self.paused
                    pygame.mixer.music.pause() if self.paused else pygame.mixer.music.unpause()

                if not self.paused and self.shake_frames == 0:
                    if event.key == pygame.K_LEFT: self.snake.move_left()
                    elif event.key == pygame.K_RIGHT: self.snake.move_right()
                    elif event.key == pygame.K_UP: self.snake.move_up()
                    elif event.key == pygame.K_DOWN: self.snake.move_down()

    def update(self):
        if self.paused: return

        if self.shake_frames > 0:
            self.shake_frames -= 1
            if self.shake_frames == 0:
                self.engine.states['game_over'].set_score(self.score)
                self.engine.change_state('game_over')
                self.reset_game()
            return

        self.snake.walk()
        self.apple.update()

        # Eat Apple Logic
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.resource_manager.play_sound('ding')
            
            # Points logic
            points = 5 if self.apple.is_golden else 1
            self.score += points
            
            # Juice: Particles
            color = (255, 215, 0) if self.apple.is_golden else (255, 50, 50)
            self.particles.emit(self.apple.x, self.apple.y, color)
            
            self.snake.increase_length()
            
            # Pass snake body to prevent spawning inside the snake
            body = list(zip(self.snake.x, self.snake.y))
            self.apple.randomize_position(body)
            
            if self.snake.length % 4 == 0:
                self.current_speed += 1 

        # Collisions
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.trigger_crash()
                return

        if not (0 <= self.snake.x[0] < WINDOW_WIDTH and 0 <= self.snake.y[0] < WINDOW_HEIGHT):
            self.trigger_crash()
            return

        self.engine.clock.tick(self.current_speed)

    def draw(self, surface):
        offset_x = random.randint(-10, 10) if self.shake_frames > 0 else 0
        offset_y = random.randint(-10, 10) if self.shake_frames > 0 else 0

        temp_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        temp_surface.blit(self.bg_image, (0, 0)) if self.bg_image else temp_surface.fill((110, 110, 5))

        self.apple.draw(temp_surface)
        self.snake.draw(temp_surface)
        self.particles.update_and_draw(temp_surface)

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        temp_surface.blit(score_text, (WINDOW_WIDTH - 150, 10))

        if self.paused:
            pause_text = pygame.font.SysFont('arial', 50, bold=True).render("PAUSED", True, WHITE)
            temp_surface.blit(pause_text, (WINDOW_WIDTH//2 - 100, 350))

        surface.blit(temp_surface, (offset_x, offset_y))