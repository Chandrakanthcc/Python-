class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursively(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete_recursively(node.right, min_node.key)

        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=' ')


# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)
    print("\nPreorder Traversal:")
    tree.preorder_traversal(tree.root)
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)

    print("\nAfter deleting 30:")
    tree.delete(30)
    tree.inorder_traversal(tree.root)
