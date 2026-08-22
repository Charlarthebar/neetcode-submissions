class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lMax = [0] * n
        rMax = [0] * n

        cur = 0
        for i, h in enumerate(height):
            lMax[i] = cur
            cur = max(cur, h)
            
        cur = 0
        for i in range(len(height) - 1, -1, -1):
            rMax[i] = cur
            cur = max(cur, height[i])
        # print(lMax)
        # print(rMax)
        res = 0
        for i, h in enumerate(height):
            l, r = lMax[i], rMax[i]
            if l == 0 or r == 0 or h >= l or h >= r:
                continue
            res += min(l, r) - h
        return res