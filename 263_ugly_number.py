class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n <= 5:
            return True

        nums = (2, 3, 5)
        for num in nums:
            if n % num == 0 and (n//num in nums or self.isUgly(n//num)):
                return True
        return False


n = 14
output = False


obj = Solution()
res = obj.isUgly(n)
print(res)
print(output)
print(res == output)
