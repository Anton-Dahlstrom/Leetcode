class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        memo = [0]*len(prices)

        def dfs(i):
            pass
        for i in reversed(range(0, len(prices)-1)):
            price = prices[i]
            if price < prices[i+1]:
                memo[i] = prices[i+1] - price

        print(memo)
        print(prices)
        # [1,2,3,0,2]
        # [1,1,0,2,0]


prices = [1, 2, 3, 0, 2]
output = 3

obj = Solution()
res = obj.maxProfit(prices)
print(res)
print(res == output)
