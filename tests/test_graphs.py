import unittest

from Graphs.graph import Graph
from Graphs.graph_node import GraphNode


def construct_circular_graph():
    """
     1 -> 2
     ^    |
     |    v
        3

    """
    graph = Graph()
    graph_node_1 = GraphNode(1)
    graph_node_2 = GraphNode(2)
    graph_node_3 = GraphNode(3)
    graph_node_1.add_node(graph_node_2)
    graph_node_2.add_node(graph_node_3)
    graph_node_3.add_node(graph_node_1)
    graph.add_nodes([graph_node_1, graph_node_2, graph_node_3])


class GraphsTest(unittest.TestCase):
    pass
