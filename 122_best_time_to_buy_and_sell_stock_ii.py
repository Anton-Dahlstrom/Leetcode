class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                res += prices[i+1]-prices[i]
        return res


prices = [7, 1, 5, 3, 6, 4]
output = 7

obj = Solution()
res = obj.maxProfit(prices)
print(res)
print(output)
print(res == output)
