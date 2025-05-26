class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cutting = max(n, m)
        if cutting <= k:
            return 0
        cutsize = cutting - k
        return (cutting - cutsize) * cutsize


n = 6
m = 5
k = 5

output = 5

obj = Solution()
res = obj.minCuttingCost(n, m, k)
print(res)
print(output)
print(res == output)
