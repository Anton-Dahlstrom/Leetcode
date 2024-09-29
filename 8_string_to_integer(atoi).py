class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        i = 0
        positive = True
        maxint = 2**31
        maxlen = len(str(maxint))
        res = ""
        if s[0] == "-":
            positive = False
            i = 1
        elif s[0] == "+":
            i = 1

        while i < len(s) and s[i] == "0":
            i += 1

        while i < len(s):
            if not s[i].isdigit():
                break
            res += s[i]
            if len(res) > maxlen:
                break
            i += 1

        if not res:
            return 0
        res = int(res)
        if res >= maxint:
            if positive:
                return maxint - 1
            else:
                return maxint * -1

        if not positive:
            res *= -1
        return res


s = "  -042"
output = -42


obj = Solution()
res = obj.myAtoi(s)
print(output)
print(res)
print(res == output)
