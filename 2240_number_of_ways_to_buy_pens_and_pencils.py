class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        while total >= 0:
            res += total // cost2+1
            total -= cost1
        return res


total = 20
cost1 = 10
cost2 = 5
output = 9


obj = Solution()
res = obj.waysToBuyPensPencils(total, cost1, cost2)
print(res)
print(output)
print(res == output)
