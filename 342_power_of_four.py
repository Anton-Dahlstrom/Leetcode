class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur = 4
        e = 0
        while cur**e < n:
            e += 1
        return cur**e == n


n = 16
output = True

obj = Solution()
res = obj.isPowerOfFour(n)
print(res)
print(output)
print(res == output)
