class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = 0
        x = 64
        charRange = range(65, 91)

        def dfs(s):
            if not s:
                self.res += 1
                return
            if s[0] == "0":
                return
            dfs(s[1:])
            if len(s) > 1 and (int(s[0]) * 10) + int(s[1]) + x in charRange:
                dfs(s[2:])
        dfs(s)
        return self.res


s = "226"
output = 3
s = "27"
output = 1

obj = Solution()
res = obj.numDecodings(s)
print(res)
print(res == output)
