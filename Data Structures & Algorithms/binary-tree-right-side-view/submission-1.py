# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        levelToVals = defaultdict(list)
        def dfs(node, level):
            nonlocal levelToVals
            if not node:
                return
            levelToVals[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return
        dfs(root, 0)

        for vals in levelToVals.values():
            res.append(vals[-1])
        return res
