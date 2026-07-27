class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        prereqs = defaultdict(list)

        for a, b in prerequisites:
            prereqs[a].append(b)
        print(prereqs)


        path = set()
        res = []
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            res.append(course)
            visited.add(course)
            path.remove(course)
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
            