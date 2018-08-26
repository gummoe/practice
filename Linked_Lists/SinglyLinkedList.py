from Linked_Lists.SingleNode import SingleNode


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = SingleNode(value)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def remove(self, value):

        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def to_string(self):
        values = []

        if not self.head:
            return

        if self.head.next is None:
            return self.head.value

        current_node = self.head
        while current_node.next is not None:
            values.append(str(current_node.value))
            current_node = current_node.next
        values.append(str(current_node.value))

        return ", ".join(values)
