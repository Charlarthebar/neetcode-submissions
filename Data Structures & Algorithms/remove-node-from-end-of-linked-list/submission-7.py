# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        f = head
        dl = dummy

        for i in range(n):
            f = f.next
        
        while f:
            f = f.next
            dl = dl.next
        
        dl.next = dl.next.next
        return dummy.next
        




        