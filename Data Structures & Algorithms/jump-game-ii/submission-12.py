class Solution:
    def jump(self, nums: List[int]) -> int:
        agenda = deque([(0, 0)])
        visited = {0}
        goal = len(nums) - 1
        while agenda:
            print(agenda)
            i, jumps = agenda.popleft()
            if i == goal:
                return jumps
            
            for j in range(1, nums[i] + 1):
                if i + j not in visited:
                    agenda.append((i + j, jumps + 1))
                    visited.add(i + j)