class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def helper(l, r):
            nonlocal k
            k = k % (r - l + 1)
            if l >= r or k == 0:
                return

            for i in range(k):
                # print(i)
                # print(l + i, r - k + 1 + i)
                nums[l + i], nums[r - k + 1 + i] = nums[r - k + 1 + i], nums[l + i]
            # print(nums)
            helper(l + k, r)
            return
        helper(0, len(nums) - 1)