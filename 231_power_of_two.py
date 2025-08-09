class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bits = bin(n)
        if n > 0 and bits[2:].count("1") == 1:
            return True
        return False


n = 16
output = True

obj = Solution()
res = obj.isPowerOfTwo(n)
print(res)
print(output)
print(res == output)
