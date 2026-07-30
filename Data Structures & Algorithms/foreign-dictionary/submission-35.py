class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for w in words for c in w}

        # for w1, w2 in zip(words[:-1], words[1:]):
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return ""
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break

        res = []
        visited = set()
        def dfs(node, path):
            if node in path:
                return False
            
            if node in visited:
                return True
            path.add(node)
            
            for neighbor in adjList[node]:
                if not dfs(neighbor, path):
                    return False
            res.append(node)
            path.remove(node)
            visited.add(node)
            return True
        
        for ch in adjList:
            if not dfs(ch, set()):
                return ""
        return "".join(res[::-1])
        