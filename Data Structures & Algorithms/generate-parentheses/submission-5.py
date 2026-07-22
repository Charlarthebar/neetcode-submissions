class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, opened):
            if len(string) == 2 * n:
                if opened == 0:
                    res.append(string)
                return
            
            dfs(string + "(", opened + 1) if opened < n else None
            dfs(string + ")", opened - 1) if opened > 0 else None
        dfs("", 0)
        return res