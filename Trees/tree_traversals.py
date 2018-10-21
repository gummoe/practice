in_order_collection = []
pre_order_collection = []
post_order_collection = []


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        in_order_collection.append(node.data)
        in_order_traversal(node.right)

    return in_order_collection


def pre_order_traversal(node):
    if node is not None:
        pre_order_collection.append(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

    return pre_order_collection


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        post_order_collection.append(node.data)

    return post_order_collection



