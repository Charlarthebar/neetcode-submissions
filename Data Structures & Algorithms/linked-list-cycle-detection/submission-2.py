# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort, hare = head, head
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
                return True
            
        return False
