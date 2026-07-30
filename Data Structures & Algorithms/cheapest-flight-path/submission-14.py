class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[src] = 0

        for _ in range(k + 1):
            tmp = distances[:]
            for i, j, p in flights:
                if tmp[i] == float('inf'):
                    continue
                tmp[j] = min(tmp[j], p + distances[i])
            distances = tmp
        return distances[dst] if distances[dst] != float('inf') else -1