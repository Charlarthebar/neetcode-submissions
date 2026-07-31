class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        valToCoins = defaultdict(int)
        valToCoins[0] = 0

        for c in coins:
            valToCoins[c] = 1
            for val, numCoins in list(valToCoins.items()):
                newVal = val
                newCoins = numCoins
                while newVal <= amount:
                    # print(newVal, newCoins)
                    if newVal in valToCoins:
                        valToCoins[newVal] = min(valToCoins[newVal], newCoins)
                    else:
                        valToCoins[newVal] = newCoins
                    newVal += c
                    newCoins += 1
            # print(c, valToCoins)
            # print()
        return -1 if amount not in valToCoins else valToCoins[amount]