# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        for l in lists:
            p1 = res.next
            p2 = l
            prev1 = res
            while p1 and p2:
                if p2.val < p1.val:
                    temp = p2.next
                    prev1.next = p2
                    p2.next = p1
                    p2 = temp
                else:
                    p1 = p1.next
                prev1 = prev1.next
            if p2:
                prev1.next = p2
        return res.next


