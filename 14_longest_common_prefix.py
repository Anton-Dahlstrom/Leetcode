class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLen = float("inf")
        for s in strs:
            minLen = min(minLen, len(s))

        res = ""
        for i in range(minLen):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return res
            res += char
        return res


strs = ["flower", "flow", "flight"]
output = "fl"

obj = Solution()
res = obj.longestCommonPrefix(strs)
print(res)
print(output)
print(res == output)
