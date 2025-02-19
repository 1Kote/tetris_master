import pygame

# tamanho do jogo
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# tamanho da barra lateral
SIDE_BAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRATION = 1 - PREVIEW_HEIGHT_FRACTION

# janela completa
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDE_BAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# comportamento do jogo
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

# cores 
YELLOW = '#f1e60d'
BLUE = '#204b9b'
ORANGE = 'f07e13'
RED = '#e51b20'
PURPLE = '#7b217f'
CYAN = '#6cc6d9'
GREY = '#1C1C1C'
GREEN = '65b32e'
LINE_COLOR = '#FFFFFF'

# formas
TETROMINOS = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': PURPLE},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': YELLOW},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': BLUE},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': ORANGE},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CYAN},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': GREEN},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': RED},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}