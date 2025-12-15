class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        n = len(prices)
        res = 1
        cur = 1
        for i in range(1, n):
            if prices[i] == prices[i-1]-1:
                cur += 1
            else:
                cur = 1
            res += cur
        return res


prices = [3, 2, 1, 4]
output = 7


obj = Solution()
res = obj.getDescentPeriods(prices)
print(res)
print(output)
print(res == output)
