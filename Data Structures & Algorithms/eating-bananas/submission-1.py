class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = l + (r - l) // 2
            count = 0
            for pile in piles:
                count += (pile-1) // m + 1
            if count <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res
