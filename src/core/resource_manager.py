# src/core/resource_manager.py
import pygame
import json
import os

class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.highscore_file = "highscore.json"
        self.high_score = self.load_high_score()

    def load_image(self, name, path, has_transparency=False):
        if name not in self.images:
            try:
                img = pygame.image.load(path)
                self.images[name] = img.convert_alpha() if has_transparency else img.convert()
            except Exception as e:
                print(f"Failed to load {path}: {e}")
        return self.images.get(name)

    def load_sound(self, name, path):
        if name not in self.sounds:
            try:
                self.sounds[name] = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Failed to load {path}: {e}")
        return self.sounds.get(name)

    def play_sound(self, name):
        if name in self.sounds:
            pygame.mixer.Sound.play(self.sounds[name])

    def load_high_score(self):
        if os.path.exists(self.highscore_file):
            with open(self.highscore_file, 'r') as f:
                return json.load(f).get("high_score", 0)
        return 0

    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open(self.highscore_file, 'w') as f:
                json.dump({"high_score": self.high_score}, f)
            return True # Indicates a new high score was reached
        return False