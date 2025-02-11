import re
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while re.search(part, s):
            s = s.replace(part, "", 1)
        return s

s = "daabcbaabcbc"
part = "abc"
output= "dab"

obj = Solution()
res = obj.removeOccurrences(s, part)
print(res)
print(output)
print(res == output)