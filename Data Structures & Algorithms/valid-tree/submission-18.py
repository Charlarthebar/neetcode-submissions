class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        
        tree = {i: [] for i in range(n)}
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        visited = set()
        def has_cycle(node, prev_node):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in tree[node]:
                if neighbor == prev_node:
                    continue
                if has_cycle(neighbor, node):
                    return True
            return False
        
        return not has_cycle(0, -1) and len(visited) == n