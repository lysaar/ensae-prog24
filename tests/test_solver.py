# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_Solver(unittest.TestCase):
    def test_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        s = Solver(grid)
        #Solver.graph(grid.state)
        b = s.get_solution()
        print(b)
        #Solver.graph(grid.state)
        self.assertEqual(grid.state, [[1, 2], [3, 4], [5, 6], [7, 8]])
        

    def test_grid2(self):
        grid = Grid.grid_from_file("input/grid2.in")
        s = Solver(grid)
        Solver.graph(grid.state)
        s.get_solution() 
        Solver.graph(grid.state)       
        self.assertEqual(grid.state, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    def test_grid3(self):
        grid = Grid.grid_from_file("input/grid3.in")
        s = Solver(grid)
        Solver.graph(grid.state)
        s.get_solution()     
        Solver.graph(grid.state)   
        self.assertEqual(grid.state, [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])
    
    def test_grid4(self):
        grid = Grid.grid_from_file("input/grid4.in")
        s = Solver(grid)
        Solver.graph(grid.state)
        b = s.get_solution()
        print(b)        
        Solver.graph(grid.state)
        self.assertEqual(grid.state, [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])

if __name__ == '__main__':
    unittest.main()