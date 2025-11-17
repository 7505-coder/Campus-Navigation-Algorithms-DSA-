# tests/run_all.py
# Simple runner that calls demo functions from modules in src/
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # add src to path

try:
    from bst import demo_bst
    from graph_adjlist import demo_graph
    from dijkstra import demo_dijkstra
    from expression_tree import demo_expression
except Exception as e:
    print("Some modules missing:", e)
    raise

if __name__ == "__main__":
    print("=== BST Demo ==="); demo_bst()
    print("\n=== Graph Demo ==="); demo_graph()
    print("\n=== Dijkstra ==="); demo_dijkstra()
    print("\n=== Expression Tree ==="); demo_expression()
