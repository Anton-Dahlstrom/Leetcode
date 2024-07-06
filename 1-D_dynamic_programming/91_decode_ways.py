class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        res = 1
        fib1 = 0
        fib2 = 1
        x = 64
        charRange = range(65, 91)
        for i in range(0, len(s)):
            if s[i] == "0":
                if i < len(s)-1:
                    if s[i+1] == "0":
                        return 0
                res *= fib1 + fib2
                fib1, fib2 = 0, 1
                continue
            if i < len(s)-1:
                if s[i+1] == "0":
                    if (int(s[i]) * 10 + int(s[i+1])) + x not in charRange:
                        return 0
                    res *= fib1 + fib2
                    fib1, fib2 = 0, 1
                    continue
            if i > 0:
                if s[i-1] == "0":
                    continue
                combined = (int(s[i-1]) * 10 + int(s[i])) + x
                if combined in charRange:
                    fib1, fib2 = fib2, fib1+fib2
                else:
                    res *= fib1 + fib2
                    fib1, fib2 = 0, 1
        res *= fib1 + fib2
        return res


s = "111111111111111111111111111111111111111111111"
output = 1836311903

s = "27"
output = 1

s = "230"
output = 0

obj = Solution()
res = obj.numDecodings(s)
print(res)
print(res == output)
