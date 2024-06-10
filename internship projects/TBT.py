class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.is_threaded = False

class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
                node.left.right = node
                node.left.is_threaded = True
            else:
                self._insert(node.left, key)
        else:
            if node.right is None or node.is_threaded:
                new_node = Node(key)
                new_node.right = node.right
                new_node.is_threaded = True
                node.right = new_node
                node.is_threaded = False
            else:
                self._insert(node.right, key)

    def inorder_traversal(self):
        result = []
        current = self._leftmost(self.root)
        while current:
            result.append(current.key)
            if current.is_threaded:
                current = current.right
            else:
                current = self._leftmost(current.right)
        return result

    def preorder_traversal(self):
        result = []
        current = self.root
        while current:
            result.append(current.key)
            if current.left:
                current = current.left
            else:
                while current and (current.right is None or current.is_threaded):
                    current = current.right
                if current:
                    current = current.right
        return result

    def _leftmost(self, node):
        while node and node.left:
            node = node.left
        return node

if __name__ == "__main__":
    tb_tree = ThreadedBinaryTree()
    elements = [20, 10, 30, 5, 15, 25, 35]
    for elem in elements:
        tb_tree.insert(elem)
    print("In-order traversal:", tb_tree.inorder_traversal())
    print("Pre-order traversal:", tb_tree.preorder_traversal())
