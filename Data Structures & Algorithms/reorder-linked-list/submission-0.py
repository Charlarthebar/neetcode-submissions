# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, f, s = head, head, head
        while f and f.next:
            prev = s
            f = f.next.next
            s = s.next
        second = s.next
        s.next = None
        

        cur = None
        while second:
            temp = second.next
            second.next = cur
            cur = second
            second = temp
        second = cur

        # while second:
        #     print(second.val)
        #     second = second.next

        first = head
        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2

        return 

        

