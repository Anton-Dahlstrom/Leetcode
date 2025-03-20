from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        count = [count[k] for k in count]
        odd = 0
        even = float("inf")
        for c in count:
            if c % 2:
                odd = max(odd, c)
            else:
                even = min(even, c)
        return odd - even


s = "aaaaabbc"
output = 3

s = "tzt"
output = -1

obj = Solution()
res = obj.maxDifference(s)
print(res)
print(output)
print(res == output)
