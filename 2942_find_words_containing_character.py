class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res = []
        for i, word in enumerate(words):
            for char in word:
                if char == x:
                    res.append(i)
                    break
        return res


words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
output = [0, 2]

obj = Solution()
res = obj.findWordsContaining(words, x)
print(res)
print(output)
print(res == output)
