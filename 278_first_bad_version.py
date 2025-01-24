# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + ((r-l)//2)
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        if not isBadVersion(mid):
            mid += 1  
        return mid

n = 5
bad = 4
output= 4     

obj = Solution()
res = obj.firstBadVersion(n, bad)
print(res)
print(output)
print(res == output)