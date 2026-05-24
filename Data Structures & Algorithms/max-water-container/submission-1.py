class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = abs(l - r) * min(heights[l], heights[r])
            m = max(m, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return m

        