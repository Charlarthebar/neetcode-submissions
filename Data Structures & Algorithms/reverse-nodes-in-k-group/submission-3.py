# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l = 0
        c = head
        while c:
            c = c.next
            l += 1
        if l < k:
            return head
        dummy = head
        prev = head
        cur = prev.next
        count = 0
        while cur and count < k - 1:
            nxt = cur.next

            cur.next = prev
            prev = cur
            cur = nxt
            count += 1
        head.next = self.reverseKGroup(cur, k)
        return prev