class Solution:
    def maximum69Number(self, num: int) -> int:
        digit = 0
        temp = num
        res = -1
        while temp:
            if temp % 10 == 6:
                res = digit
            temp //= 10
            digit += 1
        if res >= 0:
            num += (3*10**res)
        return num


num = 9669
output = 9969

obj = Solution()
res = obj.maximum69Number(num)
print(res)
print(output)
print(res == output)
