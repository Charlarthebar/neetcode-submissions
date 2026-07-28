class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        swordList = set(wordList)
        if endWord not in swordList:
            return 0

        wordList.append(beginWord)
        adjList = defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                off = 0
                w1, w2 = wordList[i], wordList[j]
                for k in range(len(wordList[i])):
                    if w1[k] != w2[k]:
                        off += 1
                if off == 1:
                    adjList[w1].add(w2)
                    adjList[w2].add(w1)

        print(adjList)
        agenda = deque([beginWord])
        visited = set()
        count = 0
        while agenda:
            print(agenda)
            for _ in range(len(agenda)):
                cur = agenda.popleft()
                print(cur)
                if cur == endWord:
                    return count + 1
                for neighbor in adjList[cur]:
                    if neighbor not in visited:
                        agenda.append(neighbor)
                        visited.add(neighbor)
            count += 1
        return 0

        