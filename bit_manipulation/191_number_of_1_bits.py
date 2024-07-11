class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            temp = n
            n >>= 1
            n <<= 1
            if temp != n:
                count += 1
            n >>= 1
        return count


n = 11
output = 3

obj = Solution()
res = obj.hammingWeight(n)
print(res)
print(res == output)
