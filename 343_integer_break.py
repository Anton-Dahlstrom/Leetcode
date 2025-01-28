class Solution:
    def integerBreak(self, n: int) -> int:
        if n <=3:
            return n-1

        if n % 3 == 1:
            return  3 ** ((n-4)//3) * 2 * 2
        elif n % 3 == 2:
            return 3** ((n-2)//3) * 2
        else:
            return 3 ** (n//3)
        
n = 10
output = 36


obj = Solution()
res = obj.integerBreak(n)
print(res)
print(output)
print(res == output)