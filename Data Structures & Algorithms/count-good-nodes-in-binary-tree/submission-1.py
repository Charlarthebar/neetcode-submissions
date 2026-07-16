# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node, mmax):
            nonlocal good
            if not node:
                return 0

            good = 1 if node.val >= mmax else 0
            return good + dfs(node.left, max(mmax, node.val)) + dfs(node.right, max(mmax, node.val))
        return dfs(root, float('-inf'))
        return good