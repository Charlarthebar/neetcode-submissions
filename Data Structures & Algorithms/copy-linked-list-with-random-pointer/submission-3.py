"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def findNewNode(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]
            else:
                new = Node(node.val)
                oldToNew[node] = new
                new.next = findNewNode(node.next)
                new.random = findNewNode(node.random)
                return new
        
        if not head:
            return None

        oldToNew = {}
        start = head
        
        findNewNode(head)

        return oldToNew[start]