class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if len(words[i]) > len(words[j]):
                    continue
                size = len(words[i])
                if words[i] == words[j][:size] and words[i] == words[j][-size:]:
                    res += 1
        return res


words = ["a", "aba", "ababa", "aa"]
output = 4


obj = Solution()
res = obj.countPrefixSuffixPairs(words)
print(res)
print(output)
print(res == output)
