class Solution:
    def minimumFlips(self, n: int) -> int:
        res = 0
        s = bin(n)[2:]
        rev = bin(n)[2:]
        rev = rev[::-1]
        for i in range(len(s)):
            if s[i] != rev[i]:
                res += 1
        return res


n = 10
output = 4

obj = Solution()
res = obj.minimumFlips(n)
print(res)
print(output)
print(res == output)
