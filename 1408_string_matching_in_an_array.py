class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        trie = {}
        words.sort(key=lambda w: len(w), reverse=True)
        res = []
        charstarts = {}
        for word in words:
            substring = False
            if word[0] in charstarts:
                for start in charstarts[word[0]]:
                    substring = True
                    cur = start
                    for char in word[1:]:
                        if char not in cur:
                            substring = False
                            break
                        cur = cur[char]
                    if substring:
                        res.append(word)
                        break
            if not substring:
                level = trie
                for char in word:
                    if char not in level:
                        level[char] = {}
                        charstarts.setdefault(char, [])
                        charstarts[char].append(level[char])
                    level = level[char]
        return res


words = ["evl", "evlat", "kes", "lwkesz", "ckk", "eylwkesz", "efuw", "ickkw",
         "xnc", "evlon", "qsmd", "nmlwkeszk", "uyh", "xncme", "auze", "ixncmeqc"]
output = ["evl", "kes", "lwkesz", "ckk", "xnc", "xncme"]

obj = Solution()
res = obj.stringMatching(words)
print(res)
print(output)
print(res == output)
