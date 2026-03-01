# src/core/game_over_state.py
import pygame
from src.core.state_machine import State
from src.settings import WHITE, BLACK, WINDOW_WIDTH

class GameOverState(State):
    def __init__(self, engine, resource_manager):
        super().__init__(engine)
        self.rm = resource_manager
        self.font_large = pygame.font.SysFont('arial', 60, bold=True)
        self.font_small = pygame.font.SysFont('arial', 30, bold=True)
        self.final_score = 0
        self.is_new_high_score = False

    def set_score(self, score):
        self.final_score = score
        self.is_new_high_score = self.rm.save_high_score(score)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.engine.change_state('playing')
                elif event.key == pygame.K_ESCAPE:
                    self.engine.running = False

    def draw(self, surface):
        surface.fill(BLACK)
        title = self.font_large.render("GAME OVER", True, (255, 50, 50))
        score_text = self.font_small.render(f"Final Score: {self.final_score}", True, WHITE)
        high_score_text = self.font_small.render(f"All-Time High Score: {self.rm.high_score}", True, (0, 255, 100))
        prompt = self.font_small.render("Press ENTER to Restart or ESC to Quit", True, WHITE)
        
        surface.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 200))
        surface.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 300))
        surface.blit(high_score_text, (WINDOW_WIDTH//2 - high_score_text.get_width()//2, 350))
        
        if self.is_new_high_score:
            new_record = self.font_small.render("NEW HIGH SCORE!", True, (255, 215, 0))
            surface.blit(new_record, (WINDOW_WIDTH//2 - new_record.get_width()//2, 400))

        surface.blit(prompt, (WINDOW_WIDTH//2 - prompt.get_width()//2, 500))