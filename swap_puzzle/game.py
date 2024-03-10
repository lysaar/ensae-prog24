import pygame 
from pygame.locals import *
from grid import * 

class Game() : 

    def __init__(self,grid) -> None:
        self.grid = grid


    def game(self) : 
        g = self.grid
        m = g.m
        n = g.n
        h = 510
        w = 510
        SIZE = h, w
        RED = (255, 0, 0)
        GRAY = (150, 150, 150)

        pygame.init()
        screen = pygame.display.set_mode(SIZE,RESIZABLE)

        r=[]
        X = []
        Y=[]
        for i in range(0,h,h//n) : 
            for j in range(0,w,w//m) : 
                x = (i,j)
                y = (i+h//n,j+w//m)
                X.append(x)
                Y.append(Y)
                r.append(Rect(x[0],x[1],y[0],y[1]))
            

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            screen.fill(GRAY)
            for r1 in r : 
                pygame.draw.rect(screen, RED, r1,4)
            
            pygame.display.flip()

        pygame.quit()
                

        




g = Grid(4,2,[[1,2],[3,4],[5,6],[7,8]])
p = Game(g)
p.game()





    