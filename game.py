from settings import *
import pygame
from random import choice

class Game:

    def __init__(self):
        
        # geral
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        # linhas
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(60)

        # tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)
        

    
    # desenhando a grid do jogo(area onde as pecas de tetris vão descer)
    def draw_grid(self):

        # desenhando as linhas verticais 
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (x,0), (x,self.surface.get_height()), 1)
        
        # desenhando as linhas horizontais
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (0, y), (self.surface.get_width(), y))

        self.surface.blit(self.line_surface, (0,0))

    def run(self):

        # colorindo o fundo
        self.surface.fill(GREY)
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

class Tetromino:
    def __init__(self, shape, group):
        
        # setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']

        # criando os blocks
        self.block = [Block(group, pos, self.color) for pos in self.block_positions]

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        # geral
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE,CELL_SIZE))
        self.image.fill(color)


        # posição
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        x = self.pos.x * CELL_SIZE
        y = self.pos.y * CELL_SIZE
        self.rect = self.image.get_rect(topleft = (x,y))

