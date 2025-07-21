class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        cur = ""
        count = 0
        res = []
        for i in range(n):
            if s[i] != cur:
                cur = s[i]
                count = 1
            else:
                count += 1
            if count < 3:
                res.append(s[i])
        return "".join(res)


s = "aaabaaaa"
output = "aabaa"

obj = Solution()
res = obj.makeFancyString(s)
print(res)
print(output)
print(res == output)
