# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def invert(r):
        #     if not r:
        #         return r
        #     r.right = invert(r.left)
        #     r.left = invert(r.right)
        #     return r
        # return invert(root)

        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
        
        