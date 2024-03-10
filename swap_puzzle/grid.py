"""
This is the grid module. It contains the Grid class and its associated methods.
"""
from graph import *
from itertools import *
from numpy import * 
from heapq import *

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
        l2 = self.final()
        for i in range(m) : 
            for j in range(n) : 
                if not(l[i][j] == l2[i][j]) : 
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
        return Grid(self.m, self.n, l)

        

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for (a,b) in cell_pair_list : 
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
    
    def final(self) : 
        m = self.m 
        n = self.n 
        l = []
        ind = 1
        for i in range(m) : 
            l2 = []
            for j in range(n) : 
                l2.append(ind)
                ind += 1
            l.append(l2)
        return l
    
    def find(self,a) : 
        m = self.m 
        n = self.n 
        l = self.state
        for i in range(m) : 
            for j in range(n) : 
                if l [i][j] == a :
                    return (i,j)
        return None 



    def to_hashable(self) :    # retourne une représenttaion hashable de la grille
        return tuple(tuple(l) for l in self.state)
    
    def from_hashable(self,state) : 
        res = [list(r) for r in state] 
        return Grid(self.m,self.n,res)
    

    def grille(self) :   # Rend toutes les grilles hashées des permutations possibles à partir de self

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
            final.append(g.to_hashable())
        return final
        


    def all(self) : # Construit le graphe de tous les états possibles
        
        graph1 = Graph(self.grille())
        m = self.m
        n=self.n

        for e in graph1.nodes: #pour toutes les grilles possibles
            for ligne in range(m): #pour toutes les lignes
                for colonne in range(n): #pour toutes les colonnes
                    if ligne < m-1:
                        s1 = (self.from_hashable(e)).swap((ligne,colonne), (ligne+1,colonne))
                        b1 = s1.to_hashable()
                        if b1 not in graph1.graph[e]:
                            graph1.add_edge(e,b1)
                    if ligne > 0:
                        s2 = (self.from_hashable(e)).swap((ligne,colonne), (ligne-1,colonne))
                        b2 = s2.to_hashable()
                        if b2 not in graph1.graph[e]:
                            graph1.add_edge(e,b2)
                    if colonne < n-1:
                        s3 = (self.from_hashable(e)).swap((ligne,colonne), (ligne,colonne+1))
                        b3 = s3.to_hashable()
                        if b3 not in graph1.graph[e]:
                            graph1.add_edge(e,b3)
                    if colonne > 0:
                        s4 = (self.from_hashable(e)).swap((ligne,colonne), (ligne,colonne-1))
                        b4 = s4.to_hashable()
                        if b4 not in graph1.graph[e]:
                            graph1.add_edge(e,b4)
        return graph1

    def bfs2(self) : 
        m = self.m
        n = self.n
        graph = self.all()
        l = []
        for i in range(m) : 
            l.append(range(i*n+1, (i+1)*n+1))
        grid = Grid(m,n,l)
        return graph.bfs(self.to_hashable(),grid.to_hashable())
    
    def voisin(self) : 
        vois = [] 
        m = self.m 
        n = self.n 
        for i in range(m):
            for j in range(n):
                for l,c in [(0,1),(1,0),(-1,0),(0,-1)] :
                    new1,new2 = l+i, c+j
                    if new1 < m and new2 < n : 
                        new = [i[:] for i in self.state]
                        new[i][j], new[new1][new2] = new[new1][new2], new[i][j]
                        if new not in vois : 
                            vois.append(Grid(m,n,new).to_hashable())
        return vois


    def bfs3 (self, dst):
        dico = Graph([self.to_hashable()])
        n = self.n 
        m = self.m
        file = [(self.to_hashable(), [self.to_hashable()])]

        while file: 
            s, path = file.pop(0)
            if s == dst.to_hashable():
                return path 

            for i in range(m):
                for j in range(n):
                    if i < m-1:
                        c = (self.from_hashable(s)).swap((i,j), (i+1,j))
                        nc = c.to_hashable()
                        if nc not in dico.graph[s]:
                            dico.add_edge(s, nc)

                    if i > 0:
                        d = (self.from_hashable(s)).swap((i,j), (i-1,j))
                        nd = d.to_hashable()
                        if nd not in dico.graph[s]:
                            dico.add_edge(s, nd)

                    if j < n-1:
                        f = (self.from_hashable(s)).swap((i,j), (i,j+1))
                        nf = f.to_hashable()
                        if nf not in dico.graph[s]:
                            dico.add_edge(s, nf)

                    if j > 0:
                        h = (self.from_hashable(s)).swap((i,j), (i,j-1))
                        nh = h.to_hashable()
                        if nh not in dico.graph[s]:
                            dico.add_edge(s, nh)

            for z in dico.graph[s]:
                if z not in path:
                    file.append([z, path+[z]])

        return None

    def position(self,k) : 
        s = self.state
        m = self.m
        n = self.n 
        for i in range(m) :
            for j in range(n) :
                if s[i][j] == k : 
                    return (i,j)

    def heuristique(self) :    # différence entre grille de départ et d'arrivée
        som = 0 
        l1 = self.state 
        m = self.m
        n = self.n
        for i in range(m) : 
            for j in range(n) : 
                if not(l1[i][j] == (self.final())[i][j]) : 
                    som+=1
        return som/2
    
    def heuristique1(self) :    # distance de manhattan 
        som = 0
        m = self.m
        n = self.n
        f = self.final()
        f = Grid(m,n,f)
        for i in range(1,m*n+1) : 
            i1,j1 = self.position(i)
            i2,j2 = f.position(i)
            som += abs(i1-i2) + abs(j1-j2)
        return som/2
    
    def heuristique2(self) :    # distance 2
        som = 0
        m = self.m
        n = self.n
        f = self.final()
        f = Grid(m,n,f)
        for i in range(1,m*n+1) : 
            i1,j1 = self.position(i)
            i2,j2 = f.position(i)
            som += sqrt((i1-i2)**2+(j1-j2)**2)
        return som/2



    def bfs4(self,dst) : 
        n = self.n 
        m = self.m
        file = []
        heappush(file,(0,self.heuristique(),self.to_hashable()))
        path = [self.to_hashable()]
    
        while file: 
            (nb_swaps, _,s) = heappop(file)
            if s == dst.to_hashable():
                print(f"Mon état final est : \n {s} \n ")
                print(f"Mon chemin pour y arriver est : \n {path} \n")
                return self.from_hashable(s)
            path.append(s)
            s1 = self.from_hashable(s)
            for g in s1.voisin() : 
                if g not in path : 
                    i = self.from_hashable(g)
                    heappush(file,(nb_swaps-1,i.heuristique1(),g))
                    
                
        return None
    


        

            


    
    








    





