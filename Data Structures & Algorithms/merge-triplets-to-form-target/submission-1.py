class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        ha, hb, hc = False, False, False
        for a, b, c in triplets:
            if a <= ta and b <= tb and c <= tc:
                if a == ta:
                    ha = True
                if b == tb:
                    hb = True
                if c == tc:
                    hc = True
        return ha and hb and hc