class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge(nums, 0, len(nums) - 1)
        return nums

    def merge(self, nums, l, r):
        if l - r == 0:
            return
        m = (l + r) // 2

        self.merge(nums, l, m)
        self.merge(nums, m + 1, r)
        
        a1, a2 = nums[l:m + 1], nums[m + 1:r + 1]
        p1, p2 = 0, 0
        i = l
        while p1 < len(a1) and p2 < len(a2):
            if a1[p1] <= a2[p2]:
                nums[i] = a1[p1]
                p1 += 1
            else:
                nums[i] = a2[p2]
                p2 += 1
            i += 1
        while p1 < len(a1):
            nums[i] = a1[p1]
            p1 += 1
            i += 1
        while p2 < len(a2):
            nums[i] = a2[p2]
            p2 += 1
            i += 1
        return