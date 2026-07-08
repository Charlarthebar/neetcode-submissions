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
            if node in oldToNew:
                return oldToNew[node]
            else:
                new = Node(node.val)
                oldToNew[node] = new
                return new
        
        if not head:
            return None

        oldToNew = {None: None}
        start = head
        
        while head:
            new = findNewNode(head)
            nxt = findNewNode(head.next)
            rand = findNewNode(head.random)
            new.next = nxt
            new.random = rand
            head = head.next

        return oldToNew[start]