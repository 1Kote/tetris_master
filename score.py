from settings import *
import pygame

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDE_BAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT_FRATION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface()
        

    def run(self):
        self.display_surface.blit(self.surface,self.rect)