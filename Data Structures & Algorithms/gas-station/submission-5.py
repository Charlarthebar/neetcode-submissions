class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            # print(f'i: {i}')
            cur = gas[i] - cost[i]
            j = (i + 1) % n
            
            while cur >= 0 and j != i:
                # print(f'j: {j}')
                
                cur += gas[j] - cost[j]
                # print(f'cur: {cur}')
                if cur < 0:
                    break
                j = (j + 1) % n
            if j == i and cur >= 0:
                return i
            if j <= i:
                return -1
            i = j
            
        return -1
