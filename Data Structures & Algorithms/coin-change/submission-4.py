class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numToCount = {num: float('inf') for num in range(amount + 1)}
        numToCount[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    numToCount[num] = min(numToCount[num], numToCount[num - coin] + 1)
        return numToCount[amount] if numToCount[amount] != float('inf') else -1
            