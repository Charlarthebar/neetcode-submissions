# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def helper(node):
            nonlocal res
            if not node:
                return 0

            left, right = helper(node.left), helper(node.right)
            if abs(left - right) > 1:
                res = False
            return max(left, right) + 1
        helper(root)
        return res