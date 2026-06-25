class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mmax = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                si, hei = stack.pop()
                mmax = max(mmax, hei * (i - si))
                start = si
            if not stack or h > stack[-1][1]:
                stack.append([start, h])
            elif stack[-1][1] == h:
                stack.append([stack[-1][0], h])
        while stack:
            si, h = stack.pop()
            mmax = max(mmax, h * (len(heights) - si))
        return mmax
                