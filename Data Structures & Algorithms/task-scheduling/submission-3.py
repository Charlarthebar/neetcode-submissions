class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        for t in tasks:
            freqs[ord(t) - ord('A')] -= 1
        freqs = [n for n in freqs if n < 0]
        heapq.heapify(freqs)

        queue = deque()
        time = 0
        while freqs or queue:
            while queue and queue[0][1] <= time:
                freq, available = queue.popleft()
                heapq.heappush(freqs, freq)
            if freqs:
                freq = heapq.heappop(freqs)
                freq += 1
                if freq < 0:
                    queue.append((freq, time + n + 1))
            time += 1
        return time