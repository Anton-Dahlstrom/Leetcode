from collections import deque


class Solution:
    def maxSubstrings(self, word: str) -> int:
        chars = set()
        limbo = deque()
        res = 0
        for char in word:
            limbo.appendleft(char)
            if len(limbo) == 4:
                chars.add(limbo.pop())
            if len(limbo) == 3 and char in chars:
                res += 1
                limbo = deque()
                chars = set()
        return res


word = "abcdeafdef"
output = 2

obj = Solution()
res = obj.maxSubstrings(word)
print(res)
print(output)
print(res == output)
