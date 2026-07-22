class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(numbers):
            if not numbers:
                return [[]]

            perms = []
            for i in range(len(numbers)):
                for perm in dfs(numbers[:i] + numbers[i + 1:]):
                    perm.append(numbers[i])
                    perms.append(perm)
            return perms

        return dfs(nums)