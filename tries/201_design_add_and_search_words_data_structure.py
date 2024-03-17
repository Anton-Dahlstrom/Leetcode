class TrieNode():
    def __init__(self):
        self.nodes = {}
        self.last = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(0, len(word)):
            char = word[i]
            if char in cur.nodes:
                cur = cur.nodes[char]
            else:
                cur.nodes[char] = TrieNode()
                cur = cur.nodes[char]
        cur.last = True

    def search(self, word: str, cur=None) -> bool:
        if not cur:
            cur = self.root
        for i in range(0, len(word)):
            char = word[i]
            if char == "." and cur.nodes:
                if i == len(word) - 1:
                    for key in cur.nodes:
                        if cur.nodes[key].last:
                            return True
                    return False
                for key in cur.nodes:
                    res = self.search(word[i+1:], cur=cur.nodes[key])
                    if res:
                        return True
                return False
            if char not in cur.nodes:
                return False
            cur = cur.nodes[char]
        return cur.last

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
