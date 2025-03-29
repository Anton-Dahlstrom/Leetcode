class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += ((ord(s[i])-123) * -1) * (i+1)
        return res


s = "zaza"
output = 160

obj = Solution()
res = obj.reverseDegree(s)
print(res)
print(output)
print(res == output)
