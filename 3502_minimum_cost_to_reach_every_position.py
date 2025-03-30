class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        n = len(cost)
        res = [0]*n
        curmin = float("inf")
        for i in range(n):
            curmin = min(curmin, cost[i])
            res[i] = curmin
        return res


cost = [5, 3, 4, 1, 3, 2]
output = [5, 3, 3, 1, 1, 1]

obj = Solution()
res = obj.minCosts(cost)
print(res)
print(output)
print(res == output)
