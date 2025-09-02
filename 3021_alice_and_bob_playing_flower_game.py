class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        res = (n//2) * ((m//2)+(m % 2))
        res += (m//2) * ((n//2)+(n % 2))
        return res


n = 3
m = 2
output = 3

obj = Solution()
res = obj.flowerGame(n, m)
print(res)
print(output)
print(res == output)
