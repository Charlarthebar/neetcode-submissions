# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            total = carry
            total += l1.val if l1 else 0
            total += l2.val if l2 else 0
            cur, car = total % 10, total // 10
            newNode = ListNode(cur)
            newNode.next = dfs(l1.next if l1 else None, l2.next if l2 else None, car)
            return newNode
        return dfs(l1, l2, 0)