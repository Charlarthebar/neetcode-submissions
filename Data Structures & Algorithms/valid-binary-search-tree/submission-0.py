# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(rt, low, high):
            if not rt:
                return True
            if not (low < rt.val < high):
                return False        
            return isBST(rt.left, low, rt.val) and isBST(rt.right, rt.val, high)
        return isBST(root, float("-inf"), float("inf"))