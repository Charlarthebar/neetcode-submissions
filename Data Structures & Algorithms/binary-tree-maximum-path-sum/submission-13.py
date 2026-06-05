# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def helper(node):
            if not node:
                return 0
            c1 = helper(node.left)
            c2 = helper(node.right)
            self.res = max(self.res, node.val, node.val + max(c1, c2), node.val + c1 + c2)
            return max(node.val, node.val + max(c1, c2))
        
        helper(root)
        return self.res