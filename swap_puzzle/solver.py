from grid import Grid
import matplotlib.pyplot as plt
from random import *
from numpy import *

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self,grid=Grid(randint(1,10),randint(1,10))):
        self.g = grid 
        
    def go_from_to(self,dep, dest):    
        """ Cherche le manière naive d'ailler de dep à dest """
        res = []
        a, b = dep
        i, j = dest
        if a>i : 
            for k in range(a-i) : 
                res.append(((a-k,b),(a-k-1,b)))
                (self.g).swap((a-k,b),(a-k-1,b))
        elif i>a : 
            for k in range(i-a) : 
                res.append(((a+k,b),(a+k+1,b)))
                (self.g).swap((a+k,b),(a+k+1,b))
        if b>j : 
            for k in range(b-j) : 
                res.append(((a,b-k),(a,b-k-1)))
                (self.g).swap((a,b-k),(a,b-k-1))
        elif j>b : 
            for k in range(j-b) : 
                res.append(((a,b+k),(a,b+k+1)))
                (self.g).swap((a,b+k),(a,b+k+1))

        return res 
    
 
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        n = self.g.n
        m = self.g.m
        l = self.g.state
        sol_naive = []
        (i_dest,j_dest) = (0,0)
        

        for i in range(1,n*m+1):
            l2=array(l)
            position = where(l2==i)
            position = list(map(list,position))
            position = (position[0][0],position[1][0])
            sol_naive += self.go_from_to(position, (i_dest, j_dest))
            j_dest += 1
            if j_dest % n == 0:
                j_dest = 0
                i_dest += 1
        return sol_naive

    @staticmethod
    def graph(l) : 
        plt.matshow(array(l))
        plt.show()

    
    """ 
    La complexité est en O(n*m)
    La longueur du chemin ainsi obtenue est n'est pas optimale, il existe des solutions beaucoup plus courtes.
    Il est possible de résoudre la grille peu importe son état de départ.
    """

    
        



        

