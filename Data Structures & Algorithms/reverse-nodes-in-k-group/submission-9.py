# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lastFromPrev = dummy
        prev = head

        while prev:
            check = prev
            count = 0
            while check and count < k:
                check = check.next
                count += 1
            if count < k:
                break
            
            count = 0
            front = prev
            cur = prev.next
            while cur and count < k - 1:
                nxt = cur.next

                cur.next = prev
                prev = cur
                cur = nxt
                count += 1
            lastFromPrev.next = prev
            front.next = cur
            lastFromPrev = front
            prev = cur
        return dummy.next