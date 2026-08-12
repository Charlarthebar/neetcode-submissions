class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge(nums)

    def merge(self, arr):
        if len(arr) <= 1:
            return arr
        m = len(arr) // 2
        a1, a2 = self.merge(arr[:m]), self.merge(arr[m:])
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