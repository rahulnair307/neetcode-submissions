"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # deepcopy -> clone of the graph (exact same structe and values)
        # you can use dfs or 
        # hashmap 
        # old -> new
        oldToNew = {}

# use dfs - Create a copy of the current node, Recursively clone all its neighbors, and Return the copy.
        def clone(node):
            if node in oldToNew: # if in hashmap then we already made a clone of it
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy   # we are making a copy of the node because it is not in our hashmap
            for neighbor in node.neighbors:  # go through all the neighbors and run dfs on that neighbor
                copy.neighbors.append(clone(neighbor))
            return copy

        return clone(node) if node else None