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

            curVal = candidates[i]
            comb.append(curVal)
            helper(i + 1, total + curVal, comb)

            comb.pop()
            while i < len(candidates) and candidates[i] == curVal:
                i += 1
            helper(i, total, comb)

        helper(0, 0, [])
        return res