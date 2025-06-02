from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scnt = defaultdict(int)
        for i in range(len(s)):
            scnt[s[i]] += 1

        tcnt = defaultdict(int)
        for i in range(len(t)):
            tcnt[t[i]] += 1
            if tcnt[t[i]] > scnt[t[i]]:
                return t[i]


s = "abcd"
t = "abcde"
output = "e"

obj = Solution()
res = obj.findTheDifference(s, t)
print(res)
print(output)
print(res == output)
