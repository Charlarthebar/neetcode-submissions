class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        reach = {i: set() for i in range(1, n + 1)}
        for a, b in edges:
            if a in reach[b] or b in reach[a]:
                return [a, b]
            reach[b] |= {a} | reach[a]
            for c in reach[b]:
                reach[c] |= reach[b]
            reach[a] |= {b} | reach[b]
            for c in reach[a]:
                reach[c] |= reach[a]
