class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ""
        res = "9" * (sum//9)
        if sum % 9:
            res += str(sum % 9)
        res += "0"*(num-len(res))
        return res


num = 2
sum = 17
output = "98"


obj = Solution()
res = obj.maxSumOfSquares(num, sum)
print(output)
print(res)
print(res == output)
