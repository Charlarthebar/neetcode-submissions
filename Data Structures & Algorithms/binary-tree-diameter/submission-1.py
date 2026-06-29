# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0

        def helper(node):
            nonlocal diam
            if not node:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            diam = max(diam, l + r)
            return 1 + max(l, r)
        helper(root)
        return diam