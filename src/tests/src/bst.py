# src/bst.py
class Node:
    def __init__(self,k): self.key=k; self.left=None; self.right=None

class BST:
    def __init__(self): self.root=None
    def insert(self,k): self.root=self._insert(self.root,k)
    def _insert(self,n,k):
        if not n: return Node(k)
        if k < n.key: n.left=self._insert(n.left,k)
        else: n.right=self._insert(n.right,k)
        return n
    def inorder(self):
        res=[]
        def _in(n):
            if not n: return
            _in(n.left); res.append(n.key); _in(n.right)
        _in(self.root); return res

def demo_bst():
    b=BST()
    for k in [3,1,4,2,5]: b.insert(k)
    print("BST inorder:", b.inorder())
