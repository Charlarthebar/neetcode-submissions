# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        nodeToMax = {}
        def helper(node):
            if not node:
                print(0)
                return [0, 0, 0, 0]
            c1 = helper(node.left)
            c2 = helper(node.right)
            res = [max(node.val, max(c1[1], c1[2]) + node.val, # total max 
            max(c2[1], c2[2]) + node.val, 
            max(c1[1], c1[2]) + max(c2[1], c2[2]) + node.val, c1[3] + node.val, c2[3] + node.val, c1[3] + c2[3] + node.val), 
            node.val + c1[1], node.val + c2[2], node.val] # max going left path, max going right path, max going no path
            nodeToMax[node] = res
            print(res)
            return res
        
        helper(root)
        res = root.val
        for lst in nodeToMax.values():
            res = max(res, lst[0])
        return res
        