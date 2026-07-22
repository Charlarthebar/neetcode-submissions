class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, opened, closed):
            if len(string) == 2 * n:
                res.append(string)
                return
            
            dfs(string + "(", opened + 1, closed) if opened < n else None
            dfs(string + ")", opened, closed + 1) if opened > closed else None
        dfs("", 0, 0)
        return res