import pygame 
from pygame.locals import *
from grid import * 

class Game() : 

    def __init__(self,grid) -> None:
        self.grid = grid

    def drawBoard(self,mySurface, height, width):
        for colonne in range (width):
            for ligne in range (height):
                pygame.draw.rect(mySurface, "BLACK", (10 + ligne*50, 10 + colonne*50, 50, 50), 3)


    def game(self) : 
        grid = self.grid
        m = grid.m
        n = grid.n
        h = 640
        w = 480
        pygame.init()

        # Ouverture fenêtre

        screen = pygame.display.set_mode((h,w),RESIZABLE)   
        pygame.display.set_caption('Programme Pygame de base')

        # Remplissage de l'arrière-plan
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        self.drawBoard(screen,screen.get_width(),screen.get_height())

        Y = (0,0)
        for i in range(0,h,h//m) : 
            X = (0,0)
            for j in range(0,w,w//n) : 
                X 
                Y += ((screen.get_width())//n,(screen.get_height())//n)
                rect = pygame.draw.rect(X,Y)
                pygame.draw.rect(screen,"BLACK",rect)


        # Transférer le tout dans la fenêtre
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Boucle d'évènements
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            screen.blit(background, (0, 0))
            pygame.display.flip()


g = Grid(4,2,[[1,2],[3,4],[5,6],[7,8]])
p = Game(g)
p.game()





    