# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            else:
                res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        def helper(i):
            if i >= len(vals) or vals[i] == "N":
                return None, i + 1
            left, rightStart = helper(i + 1)
            right, nextIdx = helper(rightStart)
            node = TreeNode(vals[i], left, right)
            return node, nextIdx

        return helper(0)[0]
