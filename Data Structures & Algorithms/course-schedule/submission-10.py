class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            prereqs[a].add(b)
        print(prereqs)
        
        def cycle_check(visited, cur):
            if cur in visited:
                return True
            visited.add(cur)
            res = False
            for course in prereqs[cur]:
                res = res or cycle_check(visited, course)
            return res

        for k, v in prereqs.items():
            for val in v:
                print(k, val)
                if cycle_check({k}, val):
                    return False
        return True