class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0
        plen = len(pref)
        for word in words:
            if word[:plen] == pref:
                res += 1
        return res


words = ["pay", "attention", "practice", "attend"]
pref = "at"
output = 2

obj = Solution()
res = obj.prefixCount(words, pref)
print(res)
print(output)
print(res == output)
