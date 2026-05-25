"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new = {}

        def dfs(old):
            if old in old_new:
                return old_new[old]
            
            new = Node(old.val)
            old_new[old] = new

            for neighbor in old.neighbors:
                new.neighbors.append(dfs(neighbor))
            
            return new
        return dfs(node)

