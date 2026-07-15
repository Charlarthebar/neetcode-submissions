# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mmax = 0
        def helper(node):
            nonlocal mmax
            if not node:
                return 0
            
            left, right = helper(node.left), helper(node.right)
            mmax = max(left + right, mmax)
            return 1 + max(left, right)
        helper(root)
        return mmax