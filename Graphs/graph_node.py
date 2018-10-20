
class GraphNode:

    def __init__(self, data):
        self.data = data
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
