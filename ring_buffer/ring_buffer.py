from singly_linked_list import LinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = None
        self.end = None
        self.current_size = 0
        self.storage = LinkedList()

    def append(self, item):
        if self.current_size == self.capacity:
            curr_start = self.start
            curr_start.value = item

            if curr_start.next_node:
                self.start = curr_start.next_node
            else:
                self.start = self.storage.head

            self.end = curr_start

        if self.current_size < self.capacity:
            if self.current_size == 0:
                self.storage.add_to_tail(item)
                self.start = self.storage.head
                self.end = self.storage.head
            else:
                self.storage.add_to_tail(item)
                self.end = self.storage.tail
            self.current_size += 1

    def get(self):
        items = []
        curr_node = self.storage.head

        while curr_node:
            items.append(curr_node.value)
            curr_node = curr_node.next_node
        return items
