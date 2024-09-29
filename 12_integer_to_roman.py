class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        multi = 10 ** len(num)
        symbols = {1: "I", 5: "V", 10: "X",
                   50: "L", 100: "C", 500: "D", 1000: "M"}
        res = ""
        for n in num:
            n = int(n)
            multi /= 10
            if n == 4 or n == 9:
                n = n+1
                res += symbols[1*multi]
                res += symbols[n*multi]
                continue
            elif n > 4:
                res += symbols[5*multi]
                n -= 5
            for _ in range(n):
                res += symbols[1*multi]
        return res


num = 3749
output = "MMMDCCXLIX"

obj = Solution()
res = obj.intToRoman(num)
print(res)
print(output)
print(res == output)
