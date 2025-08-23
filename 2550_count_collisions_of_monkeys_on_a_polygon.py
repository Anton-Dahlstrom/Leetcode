class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = (10**9)+7
        res = pow(2, n, MOD)
        res -= 2
        if res < 0:
            res += MOD
        return res


n = 4
output = 14

n = 3
output = 6

obj = Solution()
res = obj.monkeyMove(n)
print(res)
print(output)
print(res == output)
