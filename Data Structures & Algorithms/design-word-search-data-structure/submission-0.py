class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        if not word:
            self.isWord = True
            return
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        if not word:
            return self.isWord
        c = word[0]
        if c == ".":
            for child in self.children.values():
                if child.search(word[1:]):
                    return True
        if c not in self.children:
            return False
        return self.children[c].search(word[1:])


        # cur = self
        # for i, c in enumerate(word):
        #     if c == ".":
        #         for anyc in cur.children.values():
        #             if anyc.search(word[i+1:]):
        #                 return True
        #     if c not in cur.children:
        #         return False
        #     cur = cur.children[c]
        # return self.isWord
