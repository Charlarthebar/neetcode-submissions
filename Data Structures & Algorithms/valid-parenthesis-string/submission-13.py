class Solution:
    def checkValidString(self, s: str) -> bool:
        opened, stars = [], []

        for i, c in enumerate(s):
            if c == "(":
                opened.append(i) 
            elif c == "*":
                stars.append(i)
            
            else:
                if opened:
                    opened.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
        
        while opened and stars:
            o, s = opened.pop(), stars.pop()
            if o > s:
                return False
        return not opened