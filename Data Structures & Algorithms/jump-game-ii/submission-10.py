class Solution:
    def jump(self, nums: List[int]) -> int:
        cur, goal = 0, len(nums) - 1
        jumps = 0

        while cur < goal:
            jumps += 1
            print(cur)
            maxDist, idx = 0, cur
            for i in range(cur + 1, cur + nums[cur] + 1):
                print(i)
                if i == goal:
                    maxDist = i + nums[i]
                    idx = goal
                    break
                if i + nums[i] > maxDist:
                    maxDist = i + nums[i]
                    idx = i
            print(maxDist)
            cur = idx
        return jumps