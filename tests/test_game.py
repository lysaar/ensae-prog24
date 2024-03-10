import sys 
sys.path.append("swap_puzzle/")
from grid import Grid
from game import Game

import unittest

class Test_Game(unittest.TestCase):

    def test_game1(self) : 
        g = Grid.grid_from_file("input/grid0.in")
        p = Game(g)
        p.game()

    def test_game2(self) : 
        g = Grid.grid_from_file("input/grid2.in")
        p = Game(g)
        p.game()

    def test_game3(self) : 
        g = Grid.grid_from_file("input/grid3.in")
        p = Game(g)
        p.game()

if __name__ == '__main__':
    unittest.main()
