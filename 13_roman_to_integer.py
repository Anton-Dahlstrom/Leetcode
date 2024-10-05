class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        prev = 0
        for char in s:
            val = symbols[char]
            if not prev:
                prev = val
                continue
            if prev >= val:
                res += prev
                prev = val
            else:
                res += (val - prev)
                prev = 0

        if prev:
            res += val

        return res


s = "MCMXCIV"
output = 1994

obj = Solution()
res = obj.romanToInt(s)
print(res)
print(output)
print(res == output)
