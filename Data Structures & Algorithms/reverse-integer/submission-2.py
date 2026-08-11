class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        pos = x >= 0
        numList = []
        x = abs(x)

        while x:
            numList.append(x % 10)
            x //= 10
        print(numList)
        target = 2**31 - 1 if pos else 2**31
        target = list(str(target))
        print(target)
        print(len(numList), len(target))
        if len(numList) == len(target):
            for n1, n2 in zip(numList, target):
                if n1 != int(n2):
                    if int(n2) < n1:
                        return 0
                    else:
                        break
            return int("".join(map(str, numList))) if pos else int("".join(map(str, numList))) * -1
        else:
            print(numList)
            return int("".join(map(str, numList))) if pos else int("".join(map(str, numList))) * -1
