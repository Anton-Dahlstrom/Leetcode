from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        res = 0
        for i in range(n):
            if coins < costs[i]:
                break
            coins -= costs[i]
            res += 1
        return res
