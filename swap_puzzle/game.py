import pygame 
from pygame.locals import *
from grid import * 

"""
Classe qui permet de gérer le jeu du puzzle en l'affichant et en permettant à l'utilisateur de faire les swaps 
"""

# Paramètres du jeu
WIDTH, HEIGHT = 700, 700
HINT_WIDTH = 400

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

class Game() : 

    def __init__(self,grid) -> None:
        self.grid = grid


    # Création cases 
    def cases(self):
        g = self.grid 
        state = g.state
        m = g.m
        n = g.n
        t = WIDTH//n 
        l = []
        for row in range(m):
            for col in range(n):
                case = pygame.Rect(col * t, row * t, t, t)
                l.append({"rect": case, "selected": False,"num" :state[row][col] }) # selcted : pour savoir si on l'a sélctionnée (au départ non)
        return l

    # Dessine la grille avec les numéros associées, la case est plus foncée si sélectionnée
    @staticmethod
    def dessine_cases(screen,cases):
        for case in cases:
            pygame.draw.rect(screen, WHITE if not case["selected"] else (200, 200, 200), case["rect"])
            pygame.draw.rect(screen, RED, case["rect"], 2)
            font = pygame.font.Font(None, 36)
            text = font.render(str(case["num"]), True, RED)
            text_rect = text.get_rect(center=case["rect"].center)
            screen.blit(text, text_rect)
    

    # Lors d'un clique, retourne la case où il a eu lieux
    @staticmethod
    def case_clique(cases, x, y):
        for case in cases:
            if case["rect"].collidepoint(x, y):
                return case
        return None
    

    # Fonctions pour vérifier que les swaps sont autorisés 
    @staticmethod
    def horizontal(origine, dst):
        return origine["rect"].y == dst["rect"].y

    @staticmethod
    def vertical(origine, dst):
        return origine["rect"].x == dst["rect"].x

    def unique_mvt(self,origine, dst):  # On ne fait qu'un swap à la fois
        t = WIDTH // ((self.grid).n)
        return (abs(origine["rect"].x - dst["rect"].x) <= t and
                abs(origine["rect"].y - dst["rect"].y) <= t)
    
    # Echange des cases 
    def swap_case(self,cases, origine, dst):
        if origine and dst:
            if Game.horizontal(origine, dst) or Game.vertical(origine, dst) and self.unique_mvt(origine, dst):   # On vérifie que le swap est possible 
                origine_indice = cases.index(origine)
                dst_indice = cases.index(dst)
                cases[origine_indice], cases[dst_indice] = cases[dst_indice], cases[origine_indice]
                origine["num"], dst["num"] = dst["num"], origine["num"]
                origine["selected"] = False
                return True

        return None

    # Test si le puzzle est réussi
    def is_solution(self, cases):
        m = (self.grid).m
        n = (self.grid).n
        t = WIDTH // n

        for row in range(m):
            for col in range(n):
                i = row * n + col
                expected_x = col * t
                expected_y = row * t

                current_case = next((case for case in cases if case["num"] == i + 1), None)

                if current_case is None or current_case["rect"].x != expected_x or current_case["rect"].y != expected_y:
                    return False

        return True
     

    # Message affiché si le puzzle est bien trié
    @staticmethod
    def message(screen):
        large1 = pygame.font.Font(None, 60)
        large2 = pygame.font.Font(None, 50)
        mess = large1.render("VICTORY", True, BLACK)
        mess2 = large2.render("Appuyez sur espace pour continuer !", True, BLACK)
        texte= mess.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        texte2 = mess2.get_rect(center=(WIDTH // 2, 2*(HEIGHT // 3)))
        screen.blit(mess, texte)
        screen.blit(mess2,texte2)
            


    def game(self) : 
        pygame.init()

        # Ouverture la fenêtre
        start_time = pygame.time.get_ticks()
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Swap Puzzle Game")
        clock = pygame.time.Clock()

        cases = self.cases()
        swaps_count = 0
        depart = None
        double_click_time = 0
            

        running = True
        while running:
            events = pygame.event.get()  # Récupérez tous les événements une seule fois

            for event in events:
                if event.type == QUIT:  
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:   # Si on clique gauche 
                    x, y = event.pos
                    case_c = Game.case_clique(cases, x, y)

                    if case_c:
                        current_time = pygame.time.get_ticks()
                        if case_c == depart and current_time - double_click_time < 500:   # Si on déselectionne une case pour en choisir une autre à bouger
                            swaps_count -= 1
                            depart["selected"] = False
                            depart = None
                        else:
                            if self.swap_case(cases, depart, case_c):  # Si c'est une case différente, on swap
                                swaps_count += 1
                            depart = case_c
                            depart["selected"] = True
                            double_click_time = current_time

                if event.type == KEYDOWN and event.key == K_SPACE:    # Si on appuie sur espace, la fenêtre se ferme
                    running = False


            screen.fill(BLACK)
            Game.dessine_cases(screen, cases)

            # Si la grille est rangée, on affiche le message 
            if self.is_solution(cases):
                end_time = pygame.time.get_ticks()
                temps = (end_time - start_time) // 1000
                Game.message(screen)
                print(f"\n VOUS AVEZ RESOLU LE PUZZLE EN {temps} SECONDES AVEC {swaps_count} SWAPS, FELICITATIONS ! \n")
                

            pygame.display.flip()
            clock.tick(30)


        pygame.quit()
                

        





    