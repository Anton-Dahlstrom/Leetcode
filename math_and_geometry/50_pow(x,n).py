class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if x < 0 and n % 2:
            negative = True

        x = abs(x)
        if n == 0 or x == 1:
            if negative:
                return -1
            return 1

        res = x
        for i in range(1, abs(n)):
            res = res * x
            if 100000 < res or res < 0.00001:
                return 0

        if negative:
            res = -res
        if n < 0:
            if res > 100000:
                return 0
            return 1/res
        return res


x = 0.00001
n = 2147483647
output = 0


obj = Solution()
res = obj.myPow(x, n)
print(res)
print(res == output)
