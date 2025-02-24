from settings import *

# componentes
from game import Game
from score import Score
from preview import Preview


class Main:
    def __init__(self):
        
        #geral
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # settando o clock pro jogo funcionar
        self.clock = pygame.time.Clock()
       

        # nome da janela do jogo
        pygame.display.set_caption('Tetris')

        # componentes
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # desligar o jogo todo
                    exit()

            # display
            self.display_surface.fill(GREY)
            
            #componentes
            self.game.run()
            self.score.run()
            self.preview.run()
 
            # atualizando a movimentação de tudo do jogo
            pygame.display.update()
            self.clock.tick()

if __name__== '__main__':
    main = Main()
    main.run()