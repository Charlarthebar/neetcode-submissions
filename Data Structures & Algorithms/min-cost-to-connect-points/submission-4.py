class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        heap = [(0, 0)] # distance, point/node
        visited = set()
        cost = 0
        while heap:
            if len(visited) == len(points):
                return cost

            dist, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            cost += dist

            for dist2, neighbor in adjList[point]:
                if neighbor not in visited:
                    heapq.heappush(heap, (dist2, neighbor))
        return cost