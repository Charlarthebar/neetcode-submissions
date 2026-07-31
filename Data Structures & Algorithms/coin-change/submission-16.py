class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(0, 0)])
        visited = set()

        while queue:
            val, numCoins = queue.popleft()
            if val == amount:
                return numCoins
            
            for c in coins:
                newVal = val + c
                newCoins = numCoins + 1
                if newVal > amount or newVal in visited:
                    continue
                queue.append((newVal, newCoins))
                visited.add(newVal)
        return -1
        
        # valToCoins = {}
        # valToCoins[0] = 0

        # for val, numCoins in list(valToCoins.items()):
        #     print(valToCoins)
        #     for c in coins:
        #         print(c)
        #         newVal = val + c
        #         if newVal > amount or newVal in valToCoins:
        #             continue

        #         newCoins = numCoins + 1
        #         if newVal == amount:
        #             return numCoins
        #         if newVal not in valToCoins:
        #             valToCoins[newVal] = newCoins
        #     print(valToCoins)

        # for c in coins:
        #     valToCoins[c] = 1
        #     for val, numCoins in list(valToCoins.items()):
        #         newVal = val
        #         newCoins = numCoins
        #         while newVal <= amount:
        #             # print(newVal, newCoins)
        #             if newVal in valToCoins:
        #                 valToCoins[newVal] = min(valToCoins[newVal], newCoins)
        #             else:
        #                 valToCoins[newVal] = newCoins
        #             newVal += c
        #             newCoins += 1
        #     # print(c, valToCoins)
        #     # print()
        # return -1 if amount not in valToCoins else valToCoins[amount]