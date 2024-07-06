class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        res = 1
        fib1 = 0
        fib2 = 1
        valRange = range(1, 27)
        for i in range(1, len(s)):
            if s[i] == "0":
                if i < len(s)-1:
                    if s[i+1] == "0":
                        return 0
                res *= fib1 + fib2
                fib1, fib2 = 0, 1
                continue
            if i < len(s)-1:
                if s[i+1] == "0":
                    if int(s[i]) * 10 + int(s[i+1]) not in valRange:
                        return 0
                    res *= fib1 + fib2
                    fib1, fib2 = 0, 1
                    continue
            if s[i-1] == "0":
                continue
            combined = int(s[i-1]) * 10 + int(s[i])
            if combined in valRange:
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
