class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        inside = False
        for i in range(len(s)):
            if s[i] == "|":
                inside = inside == False
            elif s[i] == "*":
                if not inside:
                    res += 1
        return res


s = "l|*e*et|c**o|*de|"
output = 2

obj = Solution()
res = obj.countAsterisks(s)
print(res)
print(output)
print(res == output)
