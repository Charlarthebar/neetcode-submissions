class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()
        l = r = 0

        while r < len(nums):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            while dq and dq[0] < l:
                dq.popleft()

            if r + 1 >= k:
                res.append(nums[dq[0]])
                l += 1
            r += 1
        return res