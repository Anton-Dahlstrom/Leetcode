class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(words)
        cur = 2
        res = []
        for i in range(n):
            if groups[i] != cur:
                res.append(words[i])
                cur = groups[i]
        return res


words = ["a", "b", "c", "d"]
groups = [1, 0, 1, 1]
output = ["a", "b", "c"]

obj = Solution()
res = obj.getLongestSubsequence(words, groups)
print(res)
print(output)
print(res == output)
