class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)
        distinct = set()
        res = 0
        for i in range(n):
            distinct.add(s[i])
            if len(distinct) == (i+1) % 3:
                res += 1
        return res


s = "abc"
output = 2

obj = Solution()
res = obj.residuePrefixes(s)
print(res)
print(output)
print(res == output)
