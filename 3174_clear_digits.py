class Solution:
    def clearDigits(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                if i > 0:
                    s = s[:i-1] + s[i+1:]
                    i -= 1
                else:
                    s = s[1:]
            else:
                i += 1
        return s


s = "cb34"
output = ""

obj = Solution()
res = obj.clearDigits(s)
print(res)
print(output)
print(res == output)
