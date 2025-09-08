class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        def containZero(num):
            while num >= 10:
                if not num % 10:
                    return True
                num //= 10
            return False
        for i in range(1, n):
            if not containZero(i) and not containZero(n-i):
                return [i, n-i]


n = 11
output = [2, 9]

obj = Solution()
res = obj.getNoZeroIntegers(n)
print(res)
print(output)
print(res == output)
