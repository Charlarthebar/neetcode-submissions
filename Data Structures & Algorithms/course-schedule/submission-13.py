class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            prereqs[a].add(b)
        print(prereqs)

        visited = set()
        
        def cycle_check(cur):
            if cur in visited:
                return True
            if not prereqs[cur]:
                return False

            visited.add(cur)
            res = False
            for course in prereqs[cur]:
                if cycle_check(course):
                    return True
            visited.remove(cur)
            prereqs[cur] = set()
            return res

        for k, v in prereqs.items():
            for val in v:
                print(k, val)
                if cycle_check(val):
                    return False
        return True