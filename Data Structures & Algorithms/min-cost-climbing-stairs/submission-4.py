class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            temp = first
            first = cost[i] + min(first, second)
            second = temp
        return min(first, second)