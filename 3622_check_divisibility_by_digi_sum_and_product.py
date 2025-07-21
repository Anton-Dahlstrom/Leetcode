class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitProduct = 1
        temp = n
        while temp:
            remainder = temp % 10
            digitSum += remainder
            digitProduct *= remainder
            temp //= 10
        if not n % (digitSum + digitProduct):
            return True
        return False


n = 99
output = True

obj = Solution()
res = obj.checkDivisibility(n)
print(res)
print(output)
print(res == output)
