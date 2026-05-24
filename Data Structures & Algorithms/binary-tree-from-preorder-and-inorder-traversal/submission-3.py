# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        cur_val = preorder[0]
        mid = inorder.index(cur_val)
        left_len, right_len = mid, len(preorder) - mid - 1

        node = TreeNode(cur_val)
        node.left = self.buildTree(preorder[1:1+left_len], inorder[:left_len])
        node.right = self.buildTree(preorder[1+left_len:], inorder[left_len+1:])
        return node