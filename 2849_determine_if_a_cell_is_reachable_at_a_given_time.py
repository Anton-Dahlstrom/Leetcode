class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        maxdist = max(abs(sx - fx), abs(sy - fy))
        if maxdist == 0 and t == 1:
            return False
        return maxdist <= t


sx = 2
sy = 4
fx = 7
fy = 7
t = 6
output = True

obj = Solution()
res = obj.isReachableAtTime(sx, sy, fx, fy, t)
print(res)
print(output)
print(res == output)
