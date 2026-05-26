class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for order in prerequisites:
            for i in range(len(order)):
                prereqs[order[i]] = prereqs.get(order[i], set()) | set(order[i + 1:])
        
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
                if cycle_check({k}, val):
                    return False
        return True