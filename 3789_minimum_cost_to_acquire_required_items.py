class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res = 0
        minNeed = min(need1, need2)
        if costBoth < cost1 + cost2:
            res += costBoth * minNeed
            need1 -= minNeed
            need2 -= minNeed
        res += min(costBoth, cost1) * need1
        res += min(costBoth, cost2) * need2

        return res


cost1 = 5
cost2 = 4
costBoth = 15
need1 = 2
need2 = 3

output = 22


obj = Solution()
res = obj.minimumCost(cost1, cost2, costBoth, need1, need2)
print(res)
print(output)
print(res == output)
