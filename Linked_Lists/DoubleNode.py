from Linked_Lists.SingleNode import SingleNode


class DoubleNode(SingleNode):

    def __init__(self, value):
        super().__init__(value)
        self.previous = None
