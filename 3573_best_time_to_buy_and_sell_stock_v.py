class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        n = len(prices)
        prev = [0] * n
        for i in range(k):
            lowestPrice = float("inf")
            highestPrice = float("-inf")
            cur = [0]*n
            maxprofit = 0
            for j in range(n):
                maxprofit = max(
                    maxprofit, prices[j] - lowestPrice, highestPrice - prices[j])
                if j < n-1:
                    cur[j+1] = maxprofit
                lowestPrice = min(lowestPrice, prices[j] - prev[j])
                highestPrice = max(highestPrice, prices[j] + prev[j])
            prev = cur

        return maxprofit


prices = [1, 7, 9, 8, 2]
k = 2
output = 14

obj = Solution()
res = obj.maximumProfit(prices, k)
print(res)
print(output)
print(res == output)
