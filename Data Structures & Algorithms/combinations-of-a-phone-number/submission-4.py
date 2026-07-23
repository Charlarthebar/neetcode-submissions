class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz"
            }
        if not digits:
            return []
        res = []
        def dfs(seq):
            if len(seq) == len(digits):
                res.append(seq)
                return
            i = len(seq)
            for letter in phone[digits[i]]:
                dfs(seq + letter)
        dfs("")
        return res