class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        maxval = 10**9
        cur = 1
        size = len(str(n))
        n = sorted(str(n))
        while cur <= maxval:
            cursize = len(str(cur))
            if cursize == size and sorted(str(cur)) == n:
                return True
            elif cursize > size:
                break
            cur *= 2
        return False


n = 10
output = False

obj = Solution()
res = obj.reorderedPowerOf2(n)
print(res)
print(output)
print(res == output)
