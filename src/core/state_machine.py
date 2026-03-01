import pygame
import sys
from src.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

class State:
    """Base class for all game states (Menus, Gameplay, etc.)"""
    def __init__(self, engine):
        self.engine = engine # Reference to the main game engine

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass

class GameEngine:
    """The core engine that runs the main loop and manages states."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Advanced Snake Environment")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # State management
        self.states = {}
        self.current_state = None

    def change_state(self, state_name):
        self.current_state = self.states[state_name]

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # Route logic and rendering to the active state
            if self.current_state:
                self.current_state.handle_events(events)
                self.current_state.update()
                self.current_state.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()