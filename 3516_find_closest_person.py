class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(x-z), abs(y-z)
        if d1 > d2:
            return 2
        elif d1 < d2:
            return 1
        return 0


x = 2
y = 5
z = 6
output = 2

obj = Solution()
res = obj.findClosest(x, y, z)
print(res)
print(output)
print(res == output)
