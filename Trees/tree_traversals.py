collection = []


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        collection.append(node.data)
        in_order_traversal(node.right)

    return collection


def pre_order_traversal(node):
    if node is not None:
        collection.append(node.data)
        in_order_traversal(node.left)
        in_order_traversal(node.right)

    return collection


def post_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        collection.append(node.data)

    return collection



