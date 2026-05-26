class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
            
        tree = {i: [] for i in range(n)}

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        print(tree)
        visited = set()

        def has_cycle(node, prev):
            if node in visited:
                return True
            if not tree[node]:
                return False
            
            visited.add(node)
            for neighbor in tree[node]:
                if neighbor == prev:
                    continue
                if has_cycle(neighbor, node):
                    return True
            tree[node] = []
            return False
        
        return not has_cycle(0, -1) and len(visited) == n
        