from grid import Grid
from random import *
from numpy import *

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self,grid=Grid(randint(1,10),randint(1,10))):
        self.g = grid 
        
    @staticmethod
    def go_from_to(dep, dest):
        res = []
        a, b = dep
        i, j = dest
        if i - a > 0:
            for k in range(i - a):
                res.append(((a + k, b), (a + k + 1, b)))
        else:
            for k in range(a - i):
                res.append(((a - k, b), (a - k - 1, b)))
        for k in range(j - b):
            res.append(((i, j - k), (i, j - k - 1)))

        return res
    
    @staticmethod 
    def separer(l) : 
        final = []
        for l2 in l: 
            for a in l2 : 
                final.append(a)
        return final 
 
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

        for i in range(1,n*m+1):
            (i_dest, j_dest) = (0, 0)
            l2=array(l)
            position = where(l2==i)
            position = list(map(list,position))
            position = (position[0][0],position[1][0])
            print(position)
            sol_naive += self.go_from_to(position, (i_dest, j_dest))
            j_dest += 1
            if j_dest % m == 0:
                j_dest = 0
                i_dest += 1
        return sol_naive



grid = Grid.grid_from_file("input/grid1.in")
s =Solver(grid) 
print(grid.swap_seq(s.get_solution()))


grid = Grid.grid_from_file("input/grid2.in")
print(grid)
s =Solver(grid) 
print(grid)



        

