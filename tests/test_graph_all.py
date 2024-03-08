import sys 
sys.path.append("swap_puzzle/")
from grid import Grid
from graph import Graph

import unittest 
from grid import Grid
from solver import Solver
from heapq import * 

class Test_graph_all(unittest.TestCase):

    """def test_graph1(self):
        grid = Grid.grid_from_file("input/grid0.in")
        grid2 = Grid.grid_from_file("input/grid0.in")
        g = Grid(2,2,[[1,2],[3,4]])
        res = grid.bfs4(g)
        print(res)
        s = Solver(grid2)
        res2 = s.get_solution()
        print(res2)


    def test_graph2_seq(self):
        grid = Grid.grid_from_file("input/grid1.in")
        grid2 = Grid.grid_from_file("input/grid1.in")
        g = Grid(4,2,[[1,2],[3,4],[5,6],[7,8]])
        res = grid.bfs4(g)
        print(res)
        s = Solver(grid2)
        res2 = s.get_solution()
        print(res2)

    def test_graph3_seq(self) : 
        grid = Grid.grid_from_file("input/grid2.in")
        grid2 = Grid.grid_from_file("input/grid2.in")
        g = Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])
        res = grid.bfs4(g)
        print(res)
        s = Solver(grid2)
        res2 = s.get_solution()
        print(res2)

    def test_graph3_seq(self) : 
        grid = Grid.grid_from_file("input/grid3.in")
        grid2 = Grid.grid_from_file("input/grid3.in")
        g = Grid(4,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        res = grid.bfs4(g)
        print(res)
        s = Solver(grid2)
        res2 = s.get_solution()
        print(res2)"""

    def test_graph3_seq(self) : 
        grid = Grid.grid_from_file("input/grid4.in")
        grid2 = Grid.grid_from_file("input/grid4.in")
        g = Grid(4,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        res = grid.bfs4(g)
        print(res)
        s = Solver(grid2)
        res2 = s.get_solution()
        #print(res2)

    def test_graph3_seq(self) : 
        grid = Grid.grid_from_file("input/grid5.in")
        grid2 = Grid.grid_from_file("input/grid5.in")
        g = Grid(5,5,[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
        res = grid.bfs4(g)
        print(res)
        s = Solver(grid2)
        res2 = s.get_solution()
        print(res2)


if __name__ == '__main__':
    unittest.main()

