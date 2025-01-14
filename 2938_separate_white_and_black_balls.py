class Solution:
    def minimumSteps(self, s: str) -> int:
        r = 0
        l = 0
        res = 0
        while r < len(s):
            if s[r] == "0":
                res += r-l
                l += 1
            r += 1
        return res


s = "1010"
output = 3

obj = Solution()
res = obj.minimumSteps(s)
print(res)
print(output)
print(res == output)