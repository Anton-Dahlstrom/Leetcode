import re


class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        n = len(code)
        hmap = {"electronics": [], "grocery": [],
                "pharmacy": [], "restaurant": []}
        for i in range(n):
            if code[i] and isActive[i] and businessLine[i] in hmap:
                if re.fullmatch(r'[A-Za-z0-9_]+', code[i]):
                    hmap[businessLine[i]].append(code[i])
        keys = sorted(hmap.keys())
        res = []
        for key in keys:
            res += sorted(hmap[key])
        return res


code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"]
businessLine = ["grocery", "electronics", "invalid"]
isActive = [False, True, True]

output = ["ELECTRONICS_50"]

obj = Solution()
res = obj.validateCoupons(code, businessLine, isActive)
print(res)
print(output)
print(res == output)
