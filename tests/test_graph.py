import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_graph(unittest.TestCase):
    def test_graph1(self):
        graph = Graph.graph_from_file("input/graph1.in")
        l = graph.bfs(1,14)
        self.assertEqual(l, [1,17,14])

    def test_graph2_seq(self):
        graph = Graph.graph_from_file("input/graph2.in")
        l = graph.bfs(2,19)  
        l2 = graph.bfs(1,17)  
        self.assertEqual(l, [2, 17, 19])
        self.assertEqual(l2,None)

if __name__ == '__main__':
    unittest.main()