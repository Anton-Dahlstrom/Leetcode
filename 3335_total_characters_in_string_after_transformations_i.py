class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        visited = {}

        def dfs(val, depth):
            diff = 25-val+1
            if (val+diff, depth+diff) in visited:
                return visited[(val+diff, depth+diff)]
            if depth+diff > t:
                return 1
            cur = 0
            cur += dfs(0, depth+diff) % MOD
            cur += dfs(1, depth+diff) % MOD
            visited[(val+diff, depth+diff)] = cur
            return cur

        res = 0
        for char in s:
            res += dfs(ord(char)-97, 0) % MOD
            res %= MOD
        return res % MOD


s = "abcyy"
t = 2
output = 7


obj = Solution()
res = obj.lengthAfterTransformations(s, t)
print(res)
print(output)
print(res == output)
