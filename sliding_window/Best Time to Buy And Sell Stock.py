
prices = [7,1,5,3,6,4]
# output = 5

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        highestPayout = 0
        lowestPrice = prices[0]
        for price in prices[1:]:
            lowestPrice = min(price, lowestPrice)
            payout = price - lowestPrice
            highestPayout = max(payout, highestPayout)
        return highestPayout
    
obj = Solution()
answer = obj.maxProfit(prices)
print(answer)