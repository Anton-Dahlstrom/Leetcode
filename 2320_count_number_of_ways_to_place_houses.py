class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        a, b, c = 1, 2, 1
        for _ in range(n-1):
            a, b, c = (a+b+c) % MOD, ((a*2)+b) % MOD, a % MOD
        return (a+b+c) % MOD


n = 5
output = 169

obj = Solution()
res = obj.countHousePlacements(n)
print(res)
print(output)
print(res == output)
