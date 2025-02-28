class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        next = 0
        while len(num) > 1:
            for i in range(len(num)):
                next += int(num[i])
            num = str(next)
            next = 0
        return int(num)


num = 38
output = 2

obj = Solution()
res = obj.addDigits(num)
print(res)
print(output)
print(res == output)
