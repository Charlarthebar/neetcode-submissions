class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        l, r = 0, len(height) - 1
        water = 0

        while r > l:
            if height[l] < height[r]:
                if height[l] >= maxL:
                    maxL = max(maxL, height[l])
                else:
                    water += maxL - height[l]
                l += 1
            else:
                if height[r] >= maxR:
                    maxR = max(maxR, height[r])
                else:
                    water += maxR - height[r]
                r -= 1
        return water