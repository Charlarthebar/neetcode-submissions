# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        f, s = head, head
        length = 0

        while s:
            length += 1 
            s = s.next
        print(length)
        
        
        for i in range(length - n):
            prev = f
            f = f.next
        
        if length-n == 0:
            if f.next is None:
                return None
            prev = dummy
            prev.next = f.next
            return dummy.next

        # remove f node
        f = f.next
        prev.next = f

        return dummy.next

        