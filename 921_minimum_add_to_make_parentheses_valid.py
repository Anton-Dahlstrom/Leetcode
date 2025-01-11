class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        res = 0
        for c in s:
            if c == "(":
                open += 1
            else:
                if not open:
                    res += 1
                else:
                    open -= 1
        res += open
        return res


s = "((("
output = 3

obj = Solution()
res = obj.minAddToMakeValid(s)
print(res)
print(output)
print(res == output)
