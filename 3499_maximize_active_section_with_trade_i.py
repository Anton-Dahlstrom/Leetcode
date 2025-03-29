class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        prevsize = 0
        size = 0
        res = -1
        best = 0
        s = "1" + s + "1"
        n = len(s)
        blocks = 0
        for i in range(1, n):
            if s[i] == "1":
                res += 1
                if s[i-1] != "1":
                    best = max(best,  prevsize + size)
                    prevsize = size
                    size = 0
                    blocks += 1
            else:
                size += 1
        if blocks < 2:
            return res
        return res + best


s = "1000100"
output = 7


obj = Solution()
res = obj.maxActiveSectionsAfterTrade(s)
print(res)
print(output)
print(res == output)
