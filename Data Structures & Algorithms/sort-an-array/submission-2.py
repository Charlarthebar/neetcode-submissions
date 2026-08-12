class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge(nums, 0, len(nums) - 1)

    def merge(self, nums, l, r):
        if l - r == 0:
            return [nums[l]]
        m = (l + r) // 2
        a1, a2 = self.merge(nums, l, m), self.merge(nums, m + 1, r)
        p1, p2 = 0, 0
        new = []
        while p1 < len(a1) and p2 < len(a2):
            if a1[p1] <= a2[p2]:
                new.append(a1[p1])
                p1 += 1
            else:
                new.append(a2[p2])
                p2 += 1
        while p1 < len(a1):
            new.append(a1[p1])
            p1 += 1
        while p2 < len(a2):
            new.append(a2[p2])
            p2 += 1
        return new