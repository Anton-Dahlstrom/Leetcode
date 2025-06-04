from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1


s = "loveleetcode"
output = 2

s = "leetcode"
output = 0

obj = Solution()
res = obj.firstUniqChar(s)
print(res)
print(output)
print(res == output)
