class Solution:
    def minSteps(self, n: int) -> int:
        if n < 2:
            return 0

        cur = {(1, 1)}  # val, clipboard
        res = 1
        while True:
            temp = set()
            res += 1
            for val, clip in cur:
                nval = val + clip
                if nval == n:
                    return res
                elif nval > n:
                    continue
                else:
                    temp.add((nval, clip))
                if val != clip:
                    temp.add((val, val))
            cur = temp


n = 12
output = 7


obj = Solution()
res = obj.minSteps(n)
print(res)
print(output)
print(res == output)
