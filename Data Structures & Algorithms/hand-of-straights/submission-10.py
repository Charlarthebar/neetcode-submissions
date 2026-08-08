class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = defaultdict(int)
        for val in hand:
            counts[val] += 1

        for n in sorted(hand):
            if n not in counts:
                continue

            while counts[n] > 0:
                for i in range(groupSize):
                    cur = n + i
                    if counts[cur] == 0:
                        return False
                    counts[cur] -= 1
        return True
                