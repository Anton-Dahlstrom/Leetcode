class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))


s = "abcd"
output = 4

obj = Solution()
res = obj.maxDistinct(s)
print(res)
print(output)
print(res == output)
