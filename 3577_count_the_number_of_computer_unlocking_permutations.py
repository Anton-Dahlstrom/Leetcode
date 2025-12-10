class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        MOD = 10**9+7
        n = len(complexity)
        if complexity[0] >= min(complexity[1:]):
            return 0
        res = 1
        for i in range(1, n):
            res *= i
            res %= MOD
        return res % MOD


complexity = [1, 2, 3]
output = 2

obj = Solution()
res = obj.countPermutations(complexity)
print(res)
print(output)
print(res == output)
