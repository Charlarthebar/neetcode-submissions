# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return 0
            return 1 + max(helper(node.left), helper(node.right))
        if not root:
            return 0
        l, r = helper(root.left), helper(root.right)
        diameter = l + r
        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))        