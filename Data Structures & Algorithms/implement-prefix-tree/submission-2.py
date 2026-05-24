class PrefixTree:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = PrefixTree()
            cur = cur.children[char]
        
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        