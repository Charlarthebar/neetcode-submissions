# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if not cur:
                return prev
            next = cur.next
            cur.next = prev
            return reverse(next, cur)

        return reverse(head, None)