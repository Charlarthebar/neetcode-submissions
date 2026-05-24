# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        traveled = set()
        def find(rt, p):
            traveled.add(rt)
            if p.val < rt.val:
                find(rt.left, p)
            elif p.val > rt.val:
                find(rt.right, p)
            else:
                return
        find(root, p)
        lca = None
        found = False
        while not found:
            if root in traveled:
                lca = root
            if q.val < root.val:
                root = root.left
            elif q.val > root.val:
                root = root.right
            else:
                found = True
        return lca