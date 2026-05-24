class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def insert(self, word):
        if not word:
            self.isWord = True
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, cur_word, visited, cur_trie):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] not in cur_trie.children or (r, c) in visited:
                return 
            
            cur_trie = cur_trie.children[board[r][c]]
            matching_char = board[r][c]
            if cur_trie.isWord:
                found.add(cur_word + matching_char)
            cur_word += matching_char
            
            visited.add((r, c))
            dfs(r + 1, c, cur_word, visited, cur_trie)
            dfs(r - 1, c, cur_word, visited, cur_trie)
            dfs(r, c + 1, cur_word, visited, cur_trie)
            dfs(r, c - 1, cur_word, visited, cur_trie)
            visited.remove((r, c))

        trie = Trie()
        for word in words:
            trie.insert(word)
        found = set()
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", set(), trie)
        return list(found)
        


            