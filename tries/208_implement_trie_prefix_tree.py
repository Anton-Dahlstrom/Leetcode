# Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

# Output
[None, None, True, False, True, None, True]


class Trie:

    def __init__(self):
        self.hmap = {}

    def insert(self, word: str) -> None:
        self.hmap[word] = 1

    def search(self, word: str) -> bool:
        if word in self.hmap:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for key in self.hmap:
            if key[0:len(prefix)] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
