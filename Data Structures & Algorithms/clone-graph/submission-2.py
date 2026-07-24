"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew = {}

        def dfs(oldNode):
            if not oldNode:
                return
            if oldNode in oldNew:
                return oldNew[oldNode]
            newNode = Node(oldNode.val)
            oldNew[oldNode] = newNode
            for neighbor in oldNode.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode

        return dfs(node)