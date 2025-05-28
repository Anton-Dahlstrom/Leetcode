from typing import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = Counter(s)
        freq = [freq[k] for k in freq]
        freq.sort(reverse=True)
        res = len(s)
        if len(freq) <= k:
            return 0
        for i in range(k):
            res -= freq[i]
        return res


s = "abc"
k = 2
output = 1

obj = Solution()
res = obj.minDeletion(s, k)
print(res)
print(output)
print(res == output)
