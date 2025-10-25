class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        res = s
        temp = list(s)
        for i in range(n):
            start = temp[:i]
            start.reverse()
            end = temp[i:]
            comb = "".join(start + end)
            res = min(res, comb)

            start = temp[:i]
            end.reverse()
            comb = "".join(start + end)

            res = min(res, comb)
        return res


s = "dcab"
output = "acdb"

obj = Solution()
res = obj.lexSmallest(s)
print(res)
print(output)
print(res == output)
