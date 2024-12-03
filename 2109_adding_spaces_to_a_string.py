class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res = ""
        prev = 0
        for space in spaces:
            res += s[prev:space] + " "
            prev = space
        res += s[prev:]
        res.rstrip()
        return res


s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
output = "Leetcode Helps Me Learn"

obj = Solution()
res = obj.addSpaces(s, spaces)
print(res)
print(output)
print(res == output)
