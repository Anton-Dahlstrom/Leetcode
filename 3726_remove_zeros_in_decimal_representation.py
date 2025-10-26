class Solution:
    def removeZeros(self, n: int) -> int:
        res = []
        for char in str(n):
            if char != "0":
                res.append(char)
        return int("".join(res))


n = 1020030
output = 123

obj = Solution()
res = obj.removeZeros(n)
print(res)
print(output)
print(res == output)
