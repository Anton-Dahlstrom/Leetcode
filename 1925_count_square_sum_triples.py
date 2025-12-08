import math


class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                cSquare = (a*a) + (b*b)
                c = math.sqrt(cSquare)
                if c <= n and int(c) == c:
                    res += 1
                    if a != b:
                        res += 1
        return res


n = 10
output = 4

obj = Solution()
res = obj.countTriples(n)
print(res)
print(output)
print(res == output)
