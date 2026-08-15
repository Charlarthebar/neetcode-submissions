class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rank = {num : 1 for num in nums}
        par = {num : num for num in nums}

        def find(n1):
            if n1 == par[n1]:
                return n1
            par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
            
            par[p2] = par[p1]
            rank[p1] += rank[p2]
        
        have = set()
        for num in nums:
            if num - 1 in have:
                union(num, num - 1)
            if num + 1 in have:
                union(num, num + 1)
            have.add(num)

        # print(rank)
        # print(par)
        return max(list(rank.values()))