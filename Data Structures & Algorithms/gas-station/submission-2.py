class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cur, start = 0, 0
        total = 0
        
        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            cur += diff

            if cur < 0:
                cur = 0
                start = i + 1
        return start if total >= 0 else -1