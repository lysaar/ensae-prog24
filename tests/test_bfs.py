import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph
from grid import Grid


g = Grid.grid_from_file("input/grid1.in")
graph1 = g.all()
print(graph1)
dst =[[1,2],[3,4],[5,6],[7,8]]
d = graph1.bfs(g,dst)
print(d)