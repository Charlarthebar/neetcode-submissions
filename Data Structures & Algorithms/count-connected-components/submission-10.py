class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {num: [] for num in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        print(graph)

        def dfs(node):
            # returns True if is part of a new connected component, False otherwise
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                # if neighbor == prev:
                #     continue
                dfs(neighbor)

            return True
        
        ccs = 0
        for i in range(n):
            if dfs(i):
                ccs += 1
            # print(ccs, i, graph, visited)
        return ccs
            