import heapq


class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        cost = 0
        step = 1
        if startPos[0] > homePos[0]:
            step = -1
        for i in range(startPos[0]+step, homePos[0]+step, step):
            cost += rowCosts[i]

        step = 1
        if startPos[1] > homePos[1]:
            step = -1
        for i in range(startPos[1]+step, homePos[1]+step, step):
            cost += colCosts[i]
        return cost


startPos = [1, 0]
homePos = [2, 3]
rowCosts = [5, 4, 3]
colCosts = [8, 2, 6, 7]
output = 18

obj = Solution()
res = obj.minCost(startPos, homePos, rowCosts, colCosts)
print(res)
print(output)
print(res == output)
