class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1


n = 10
output = 15

obj = Solution()
res = obj.smallestNumber(n)
print(res)
print(output)
print(res == output)
