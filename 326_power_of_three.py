class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        cur = 1
        while cur < n:
            cur *= 3
        return cur == n


n = 27
output = True


obj = Solution()
res = obj.isPowerOfThree(n)
print(res)
print(output)
print(res == output)
