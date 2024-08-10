class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = [0]*len(prices)

        for i in reversed(range(0, len(prices)-1)):
            price = prices[i]
            if price < prices[i+1]:
                memo[i] = prices[i+1] - price
        if len(prices) < 4:
            return max(prices) - min(prices)

        for i in range(3, len(memo)):
            memo[i] = max(memo[i-4], memo[i-3]) + memo[i]
        return max(memo)


prices = [1, 2, 3, 0, 2]
output = 3

prices = [1, 2, 4]
output = 3

prices = [2, 1]
output = 0

obj = Solution()
res = obj.maxProfit(prices)
print(res)
print(res == output)
