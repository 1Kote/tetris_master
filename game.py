from settings import *
import pygame

class Game:
    def __init__(self):
        
        # geral
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, (PADDING,PADDING))