class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1  # To handle duplicates

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key == node.key:
            node.count += 1  # Increment count if key is duplicate
        elif key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:  # key > node.key
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.count > 1:
                node.count -= 1  # Reduce count if there are duplicates
                return node
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.key = min_larger_node.key
            node.count = min_larger_node.count
            min_larger_node.count = 1
            node.right = self._delete(node.right, node.key)

        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self):
        """Inorder traversal of the BST."""
        result = []
        self._traverse_inorder(self.root, result)
        return result

    def _traverse_inorder(self, node, result):
        if node:
            self._traverse_inorder(node.left, result)
            result.append((node.key, node.count))
            self._traverse_inorder(node.right, result)

    def preorder(self):
        """Preorder traversal of the BST."""
        result = []
        self._traverse_preorder(self.root, result)
        return result

    def _traverse_preorder(self, node, result):
        if node:
            result.append((node.key, node.count))
            self._traverse_preorder(node.left, result)
            self._traverse_preorder(node.right, result)

    def postorder(self):
        """Postorder traversal of the BST."""
        result = []
        self._traverse_postorder(self.root, result)
        return result

    def _traverse_postorder(self, node, result):
        if node:
            self._traverse_postorder(node.left, result)
            self._traverse_postorder(node.right, result)
            result.append((node.key, node.count))

    def display(self, traversal_type='inorder'):
        """Display the BST based on the chosen traversal type."""
        if traversal_type == 'inorder':
            print("Inorder traversal:", self.inorder())
        elif traversal_type == 'preorder':
            print("Preorder traversal:", self.preorder())
        elif traversal_type == 'postorder':
            print("Postorder traversal:", self.postorder())
        else:
            print("Invalid traversal type. Choose from 'inorder', 'preorder', or 'postorder'.")

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert elements (including duplicates)
    elements = [50, 30, 20, 40, 70, 60, 80, 30, 50]
    for elem in elements:
        bst.insert(elem)

    # Display tree in different traversals
    print("Displaying the BST in various traversal orders:")
    bst.display('inorder')
    bst.display('preorder')
    bst.display('postorder')

    # Search for elements
    print("\nSearch results:")
    search_keys = [40, 100]
    for key in search_keys:
        result = bst.search(key)
        print(f"Search for {key}: {'Found' if result else 'Not found'}")

    # Delete elements and display the tree again
    print("\nDeleting elements and displaying the BST in inorder:")
    bst.delete(30)
    bst.delete(50)
    bst.display('inorder')
