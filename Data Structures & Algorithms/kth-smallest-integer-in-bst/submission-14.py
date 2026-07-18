# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def dfs(node, count):
            nonlocal res
            if not node:
                return count
            count = dfs(node.left, count)
            count += 1
            if count == k:
                res = node.val
            count = dfs(node.right, count)
            return count
            
        dfs(root, 0)
        return res