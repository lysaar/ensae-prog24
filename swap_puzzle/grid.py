"""
This is the grid module. It contains the Grid class and its associated methods.
"""
from graph import *
from itertools import *
from numpy import * 

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """


    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        m = self.m
        n = self.n
        l = self.state
        for i in range(m) :
            for j in range(n-1) : 
                if l[i][j] > l[i][j+1] : 
                    return False 
        return True



    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        m = self.m
        n = self.n
        l = self.state
        (i1,j1) = cell1
        (i2,j2) = cell2
        if i1>m or i2> m or j1>n or j2>n :
            raise NameError("Not allowed") 
        else : 
            tmp = l[i1][j1]
            l[i1][j1] = l[i2][j2]
            l[i2][j2] = tmp 

        

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for i in range(len(cell_pair_list)) : 
            (a,b) = cell_pair_list[i]
            self.swap(a,b)

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
    
    def to_hashable(self) :    # retourne une représenttaion hashable de la grille
        return (tuple(tuple(l)) for l in self.state)
    
    @staticmethod 
    def from_hashable(state) : 
        res = [list(r) for r in state] 
        m = len(res)
        n = len(res[0])
        return Grid(m,n,res)
    
    def all(self) : 
        final = []
        liste = []
        m = self.m
        n=self.n
        for i in range(1,m*n+1) :
            liste.append(i)
        
        for p in permutations(liste) : 
            l2 = []
            for i in range(m) : 
                a = p[i*n : (i+1)*n]
                l2.append(list(a))
            g = Grid(m,n,l2)
            final.append(g)

        l_final = []  # Création du graphe ave toutes les grilles possibles
        for g in final : 
            l_final.append(g.to_hashable())
        graph = Graph(l_final)

        for i in range(len(final)): #pour toutes les grilles possibles
            for ligne in range(m): #pour toutes les lignes
                for colonne in range(n): #pour toutes les colonnes
                    for l_plus, c_plus in [(0,1),(1,0),(-1,0),(0,-1)]: #pour toutes les opérations élementaires possibles
                        if 0 <= ligne+l_plus < m and 0 <= colonne + c_plus < n: #si la case est dans la grille
                            is_hashable = (final[i]).to_hashable()
                            final[i].swap((ligne,colonne),(ligne+l_plus,colonne+c_plus))
                            graph.add_edge(is_hashable, final[i].to_hashable())
        
        return graph

 


    


    

    

        





