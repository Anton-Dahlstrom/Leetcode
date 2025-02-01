from collections import defaultdict
class Solution:
    def findValidPair(self, s: str) -> str:
        counts = defaultdict(int) 
        for i in range(len(s)):
            counts[s[i]]+=1

        for i in range(len(s)-1):
            if s[i] != s[i+1] and counts[s[i]] == int(s[i]) and counts[s[i+1]] == int(s[i+1]):
                return s[i] + s[i+1]
        return ""

s = "3331"
output = "31"

obj = Solution()
res = obj.findValidPair(s)
print(res)
print(output)
print(res == output)
