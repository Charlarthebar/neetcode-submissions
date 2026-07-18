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
            print(node.val, count)
            count += 1
            print(node.val, count)
            if count == k and not res:
                res = node.val
            count = dfs(node.right, count)
            print(node.val, count)
            return count
        dfs(root, 0)
        return res