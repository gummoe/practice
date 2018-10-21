import unittest

from Graphs.graph import Graph
from Graphs.graph_node import GraphNode
from Graphs.graph_traversals import breadth_first_search


def construct_undirected_graph():
    """
     1 -> 2
     ^    |
     |    v
      --- 3 ---> 4
          |
          V
          5

    """
    graph = Graph()
    graph_node_1 = GraphNode(1)
    graph_node_2 = GraphNode(2)
    graph_node_3 = GraphNode(3)
    graph_node_4 = GraphNode(4)
    graph_node_5 = GraphNode(5)
    graph_node_1.add_node(graph_node_2)
    graph_node_2.add_node(graph_node_3)
    graph_node_3.add_node(graph_node_1)
    graph_node_3.add_node(graph_node_4)
    graph_node_4.add_node(graph_node_5)
    graph.add_nodes([graph_node_1, graph_node_2, graph_node_3])
    return graph


class GraphsTest(unittest.TestCase):

    def test_bfs_search_value_in_graph(self):
        graph = construct_undirected_graph()

        self.assertTrue(breadth_first_search(graph, 2))

    def test_bfs_search_value_not_in_graph(self):
        graph = construct_undirected_graph()

        self.assertFalse(breadth_first_search(graph, 18))
