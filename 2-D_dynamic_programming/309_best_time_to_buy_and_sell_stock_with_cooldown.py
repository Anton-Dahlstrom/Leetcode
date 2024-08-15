class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        trades = [0]*len(prices)
        lowestPrice = prices[0]

        for i in range(0, len(prices)):
            if i > 3:
                first = prices[i-1] + min(trades[i-4:i-2])
                second = min(prices[i-2:i]) + trades[i-4]
                best = min(first, second)
                prices[i-3] = prices[i-3] + trades[i-5]
                lowestPrice = min(lowestPrice, prices[i-3])
            elif i > 2:
                best = prices[i-1] + trades[i-3]
            else:
                best = min(prices[:i+1])
            lowestPrice = min(lowestPrice, prices[i])
            trade = min(best, lowestPrice) - prices[i]
            res = min(res, trade)
            trades[i] = min(trade, res)
        return abs(res)


prices = [6, 5, 4, 8, 6, 8, 7, 8, 9, 4, 5]
output = 6

obj = Solution()
res = obj.maxProfit(prices)
print(res)
print(res == output)
