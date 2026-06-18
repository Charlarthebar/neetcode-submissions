class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            print(stack)
            temp = temperatures[i]
            if not stack:
                stack.append((temp, i))
                continue
            while stack and stack[-1][0] <= temp:  
                t, idx = stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temp, i))
            
        return res