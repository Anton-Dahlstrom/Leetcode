class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror = int(str(n)[::-1])
        return abs(n-mirror)


n = 25
output = 27

obj = Solution()
res = obj.mirrorDistance(n)
print(res)
print(output)
print(res == output)
