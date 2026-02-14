from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        singles = set()
        doubles = set()
        for word in words:
            if len(word) < k:
                continue
            prefix = word[:k]
            if prefix in singles:
                doubles.add(prefix)
            else:
                singles.add(prefix)
        return len(doubles)


words = ["apple", "apply", "banana", "bandit"]
k = 2
output = 2


obj = Solution()
res = obj.prefixConnected(words, k)
print(res)
print(output)
print(res == output)
