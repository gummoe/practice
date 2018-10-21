bfs_queue = []


def depth_first_search(graph, val):
    pass


def breadth_first_search(graph, val):
    return bfs_node_search(graph.nodes[0], val)


def bfs_node_search(node, val):
    if node.data == val:
        return True

    for node in node.nodes:
        bfs_queue.append(node)

    if len(bfs_queue) > 1:
        return bfs_node_search(bfs_queue.pop(0), val)
    else:
        return False
