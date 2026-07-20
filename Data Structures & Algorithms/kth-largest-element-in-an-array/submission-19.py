class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        target = len(nums) - k

        while l <= r:
            comp = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < comp:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p < target:
                l = p + 1
            elif p > target:
                r = p - 1
            else:
                return nums[p]