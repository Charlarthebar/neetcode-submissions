class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for ch in s:
            if ch in d:
                if not stack:
                    return False
                if d[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
            print(stack)
        
        return not stack