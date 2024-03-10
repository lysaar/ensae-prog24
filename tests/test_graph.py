import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

"""
Tests des fonctions graph_from_file_path et bfs 
"""

class Test_graph(unittest.TestCase):
    def test_graph1(self):
        graph = Graph.graph_from_file("input/graph1.in")
        res = Graph.graph_from_file_path("input/graph1.path.out",1,14)
        l = graph.bfs(1,14)
        self.assertEqual(l, res)

    def test_graph2_seq(self):
        graph = Graph.graph_from_file("input/graph2.in")
        res = Graph.graph_from_file_path("input/graph2.path.out",2,19)
        res2 = Graph.graph_from_file_path("input/graph2.path.out",1,17)
        l = graph.bfs(2,19)  
        l2 = graph.bfs(1,17)  
        self.assertEqual(l, res)
        self.assertEqual(l2,res2)

if __name__ == '__main__':
    unittest.main()