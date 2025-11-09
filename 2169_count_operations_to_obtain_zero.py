class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 and num2:
            if num1 < num2:
                num2 -= num1
            else:
                num1 -= num2
            res += 1
        return res


num1 = 2
num2 = 3
output = 3

obj = Solution()
res = obj.countOperations(num1, num2)
print(res)
print(output)
print(res == output)
