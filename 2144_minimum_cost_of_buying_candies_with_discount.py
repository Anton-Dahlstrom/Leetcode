from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n = len(cost)
        res = 0
        for i in range(n):
            if not (i+1) % 3:
                continue
            res += cost[i]
        return res
