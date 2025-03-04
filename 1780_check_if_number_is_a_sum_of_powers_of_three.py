class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        cur = 1
        while cur <= n:
            cur *= 3

        while cur and n:
            cur //= 3
            if cur <= n:
                n -= cur

        if n:
            return False
        return True


n = 91
output = True


obj = Solution()
res = obj.checkPowersOfThree(n)
print(res)
print(output)
print(res == output)
