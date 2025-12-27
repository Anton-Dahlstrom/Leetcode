from collections import defaultdict


class Solution:
    def minCost(self, s: str, cost: list[int]) -> int:
        n = len(s)
        totalCosts = 0
        hmap = defaultdict(int)
        highestCost = 0
        for i in range(n):
            hmap[s[i]] += cost[i]
            totalCosts += cost[i]
            highestCost = max(highestCost, hmap[s[i]])
        return totalCosts - highestCost


s = "aabaac"
cost = [1, 2, 3, 4, 1, 10]
output = 11

obj = Solution()
res = obj.minCost(s, cost)
print(res)
print(output)
print(res == output)
