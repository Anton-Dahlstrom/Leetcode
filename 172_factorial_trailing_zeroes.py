class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 1
        for i in range(1, n+1):
            total *= i
        res = 0
        while total % 10 == 0:
            res += 1
            total //= 10
        return res


n = 5
output = 1

obj = Solution()
res = obj.trailingZeroes(n)
print(res)
print(output)
print(res == output)
