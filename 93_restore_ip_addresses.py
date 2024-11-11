class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) < 4:
            return res

        def dfs(s, i, needed):
            if not needed:
                if int(s[i:]) > 255 or (len(s)-i > 1 and s[i] == "0"):
                    return
                res.append(s)
                return
            if s[i] == "0" and len(s) - i > 1:
                dfs(s[:i+1] + "." + s[i+1:], i + 2, needed - 1)
                return
            start = i
            for i in range(i, min(i+4, len(s) - 1)):
                if needed == 1 and s[i+1] == "0" and i < len(s) - 2:
                    continue
                if len(s) - i - 1 > needed * 4:
                    continue
                if int(s[start:i+1]) > 255:
                    continue
                dfs(s[:i+1] + "." + s[i+1:], i + 2, needed - 1)

        dfs(s, 0, 3)
        return res


s = "101023"
output = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

obj = Solution()
res = obj.restoreIpAddresses(s)
print(res)
print(output)
print(res == output)
