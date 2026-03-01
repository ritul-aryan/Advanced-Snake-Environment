# main.py
import pygame
from src.core.state_machine import GameEngine, State
from src.core.resource_manager import ResourceManager
from src.core.playing_state import PlayingState
from src.core.game_over_state import GameOverState
from src.settings import WHITE, BLACK, WINDOW_WIDTH

class MainMenuState(State):
    def __init__(self, engine):
        super().__init__(engine)
        self.font_large = pygame.font.SysFont('arial', 50, bold=True)
        self.font_small = pygame.font.SysFont('arial', 30, bold=True)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.engine.change_state('playing')
                elif event.key == pygame.K_ESCAPE:
                    self.engine.running = False

    def draw(self, surface):
        surface.fill(BLACK)
        title = self.font_large.render("ADVANCED SNAKE", True, (0, 255, 100))
        prompt = self.font_small.render("Press ENTER to Start", True, WHITE)
        
        surface.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 300))
        surface.blit(prompt, (WINDOW_WIDTH//2 - prompt.get_width()//2, 400))

if __name__ == "__main__":
    engine = GameEngine()
    resource_manager = ResourceManager()

    print("Loading assets into memory...")
    resource_manager.load_image('background', 'resources/images/background.jpg')
    resource_manager.load_image('block', 'resources/images/block.jpg')
    resource_manager.load_image('apple', 'resources/images/Apple.png', has_transparency=True) 
    
    resource_manager.load_sound('ding', 'resources/sounds/ding.mp3')
    resource_manager.load_sound('crash', 'resources/sounds/crash.mp3')
    
    try:
        pygame.mixer.music.load('resources/sounds/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)
    except Exception as e:
        print(f"Could not load background music: {e}")

    # Register States
    engine.states['menu'] = MainMenuState(engine)
    engine.states['playing'] = PlayingState(engine, resource_manager)
    engine.states['game_over'] = GameOverState(engine, resource_manager) # Updated!
    
    engine.change_state('menu')
    engine.run()