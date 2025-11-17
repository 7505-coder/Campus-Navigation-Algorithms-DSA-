# src/bst.py
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def inorder(self):
        res = []
        def _in(node):
            if not node: return
            _in(node.left); res.append(node.key); _in(node.right)
        _in(self.root)
        return res

def demo_bst():
    # sample demo using IDs
    b = BST()
    for k in [3,1,4,2,5]:
        b.insert(k)
    print("--- BST Inorder ---")
    print(b.inorder())
