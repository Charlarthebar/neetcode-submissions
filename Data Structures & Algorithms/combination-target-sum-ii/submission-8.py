class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        print(candidates)
        res = []

        def helper(i, total, comb):
            if total == target:
                res.append(comb[:])
                return
            if total > target or i >= len(candidates):
                return

            comb.append(candidates[i])
            helper(i + 1, total + candidates[i], comb)

            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, total, comb)

        helper(0, 0, [])
        return res