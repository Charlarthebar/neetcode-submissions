class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()
        res = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1
            if len(visited) == n:
                return res
            for n2, w2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (w1 + w2, n2))
        print(visited)
        return -1