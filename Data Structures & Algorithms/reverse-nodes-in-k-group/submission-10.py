# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getkth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = getkth(prevGroup, k)
            if not kth:
                break
            
            nextGroup = kth.next
            prev, cur = kth.next, prevGroup.next
            while cur != nextGroup:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next