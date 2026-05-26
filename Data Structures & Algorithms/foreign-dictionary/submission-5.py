class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        print(graph)

        queue = [char for char in indegree if indegree[char] == 0]
        res = []

        while queue:
            char = queue.pop(0)
            res.append(char)

            for neigh in graph[char]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)



        visited = set()
        ordering = ""
        def dfs(node):
            nonlocal ordering
            if node in visited:
                return
            
            visited.add(node)
            ordering += node
            for neighbor in graph[node]:
                dfs(neighbor)
            return
        dfs(words[0][0])
        for k, v in graph.items():
            print("here")
            if k not in graph.values():
                ordering += k
        return ordering

        # chars = set()
        # max_len = max(len(word) for word in words)
        # new_words = ["" for _ in range max_len]

        # for word in words:
        #     for i, char in enumerate(word):
        #         new_words[i].append(char)
        #         chars.add(char)
        
        # words += new_words
        # graph = {char: set() for char in chars}
        # for word in words:
        #     for i in range(len(word)):
        #         char1 = word[i]
        #         for j in range(i + 1, len(word)):
        #             char2 = word[j]
        #             graph[char1].add(char2)

        # edges_into = {}