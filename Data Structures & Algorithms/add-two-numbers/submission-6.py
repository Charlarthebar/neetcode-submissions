# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        prev = ListNode()
        head = prev
        cur, carry = 0, 0
 
        while p1 and p2:
            newVal = p1.val + p2.val + carry
            cur, carry = newVal % 10, newVal // 10
            prev.next = ListNode(cur)
            prev, p1, p2 = prev.next, p1.next, p2.next
        
        while p1:
            newVal = p1.val + carry
            cur, carry = newVal % 10, newVal // 10
            prev.next = ListNode(cur)
            prev, p1 = prev.next, p1.next
        while p2: 
            newVal = p2.val + carry
            cur, carry = newVal % 10, newVal // 10
            prev.next = ListNode(cur)
            prev, p2 = prev.next, p2.next
            
        if carry:
            prev.next = ListNode(carry)
        return head.next