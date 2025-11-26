class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = "0"
        x = 0
        for d in str(n):
            if d != "0":
                num += d
            x += int(d)

        return int(num) * x


n = 10203004
output = 12340

obj = Solution()
res = obj.sumAndMultiply(n)
print(res)
print(output)
print(res == output)
