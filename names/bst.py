"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# from queue import Queue
# from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        else:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        highest = self.value
        if not self.right:
            return highest
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if not node:
            return

        queue = Queue()
        queue.enqueue(node)

        while queue.size > 0:
            curr_node = queue.dequeue()
            print(curr_node.value)

            if curr_node.left:
                queue.enqueue(curr_node.left)
            if curr_node.right:
                queue.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node is None:
            return

        stack = Stack()
        stack.push(node)

        while stack.size > 0:
            curr_node = stack.pop()
            print(curr_node.value)

            if curr_node.left:
                stack.push(curr_node.left)
            if curr_node.right:
                stack.push(curr_node.right)
