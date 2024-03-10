import sys 
sys.path.append("swap_puzzle/")
from grid import Grid

import unittest 
from heapq import * 

"""
Tests de la fonction bfs4 
Les mêmes peuvent être effectuées sur bfs2 et bfs3 pour observer que respectivement, 
pour les matrices 3x3 et 4x4 ils nous tournent plus
"""

class Test_graph_all(unittest.TestCase):

    def test_graph1(self):
        grid = Grid.grid_from_file("input/grid0.in")
        g = Grid(2,2,[[1,2],[3,4]])
        self.assertEqual((grid.bfs4(g)).is_sorted(), True)

    def test_graph2_seq(self):
        grid = Grid.grid_from_file("input/grid1.in")
        g = Grid(4,2,[[1,2],[3,4],[5,6],[7,8]])
        self.assertEqual((grid.bfs4(g)).is_sorted(), True)
    
    def test_graph3_seq(self) : 
        grid = Grid.grid_from_file("input/grid2.in")
        g = Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual((grid.bfs4(g)).is_sorted(), True)
    
    def test_graph4_seq(self) : 
        grid = Grid.grid_from_file("input/grid3.in")
        g = Grid(4,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        self.assertEqual((grid.bfs4(g)).is_sorted(), True)

    def test_graph5_seq(self) : 
        grid = Grid.grid_from_file("input/grid4.in")
        g = Grid(4,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        self.assertEqual((grid.bfs4(g)).is_sorted(), True)

    def test_graph6_seq(self) :  # Grille 5x5 ajoutée par nous 
        grid = Grid.grid_from_file("input/grid5.in")
        g = Grid(5,5,[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
        self.assertEqual((grid.bfs4(g)).is_sorted(), True)


if __name__ == '__main__':
    unittest.main()

