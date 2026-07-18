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
        agenda = collections.deque([root])
        while agenda:
            cur = agenda.popleft()
            res.append(str(cur.val) if cur else "null")
            if cur:
                agenda.append(cur.left)
                agenda.append(cur.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        levels = data.split(",")
        print(data)
        if levels[0] == "null": 
            return None
        root = TreeNode(int(levels[0]))
        nodes = collections.deque([root])
        i = 1

        while nodes:
            cur = nodes.popleft()

            left = None
            if levels[i] != "null":
                left = TreeNode(int(levels[i]))
                nodes.append(left)
            i += 1
            
            right = None
            if levels[i] != "null":
                right = TreeNode(int(levels[i]))
                nodes.append(right)
            i += 1

            cur.left, cur.right = left, right
        return root