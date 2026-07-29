class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort()
        for i, j in tickets:
            adjList[i].append(j)

        path = ["JFK"]
        def dfs(node):
            if len(path) == len(tickets) + 1:
                return True
            for i in range(len(adjList[node])):
                neighbor = adjList[node].pop(i)
                path.append(neighbor)
                if dfs(neighbor):
                    return True
                adjList[node].insert(i, neighbor)
                path.pop()
            return False
        dfs("JFK")
        return path

