class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            temp = first
            first = min(cost[i] + first, cost[i] + second)
            second = temp
        return min(first, second)