# src/expression_tree.py
class Node:
    def __init__(self,v,l=None,r=None): self.v=v; self.l=l; self.r=r

def evalt(n):
    if not n.l and not n.r: return int(n.v)
    a=evalt(n.l); b=evalt(n.r)
    if n.v=='+': return a+b
    if n.v=='-': return a-b
    if n.v=='*': return a*b
    if n.v=='/': return a//b
def demo_expression():
    # ((3+5)*2)-4
    root=Node('-', Node('*', Node('+', Node('3'), Node('5')), Node('2')), Node('4'))
    print("Expression result:", evalt(root))
