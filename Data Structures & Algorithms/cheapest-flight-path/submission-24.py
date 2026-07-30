class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for i, j, p in flights:
            adjList[i].append((j, p))
        
        heap = [(0, src, 0)] # total price, cur airport, num stops
        visited = set()
        while heap:

            price, airport, numStops = heapq.heappop(heap)
            if airport == dst:
                return price
            visited.add((airport, numStops))
            if numStops == k + 1:
                continue
            for neighbor, p in adjList[airport]:
                if (neighbor, numStops + 1) not in visited:
                    # if neighbor == dst:
                    #     return price + p
                    heapq.heappush(heap, (price + p, neighbor, numStops + 1))
        return -1