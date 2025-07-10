from typing import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        scount = Counter(s)
        tcount = Counter(target)
        res = len(s)
        for key in tcount:
            res = min(res, scount[key] // tcount[key])
        return res


s = "ilovecodingonleetcode"
target = "code"
output = 2


obj = Solution()
res = obj.rearrangeCharacters(s, target)
print(res)
print(output)
print(res == output)
