class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        trades = [0]*len(prices)
        lowestPrice = prices[0]
        print(prices)
        # Need to update price with best trade as it becomes available
        # When i = 6 we update prices[3] by adding the best trade
        # [0, 0, -2, -2, -2, -5, -6]
        # prices when i = 5: [3, 3, 5, 0, 0, 3, 1, 4]
        # prices when i = 6: [3, 3, 5, -2, 0, 3, 1, 4]
        # We then update and look at lowestPrice
        # prices = [3, 3, 5, 0, 0, 3, 1, 4]
        # output = 6
        for i in range(0, len(prices)):
            if i > 3:
                first = prices[i-1] + min(trades[i-4:i-2])
                second = min(prices[i-2:i]) + trades[i-4]
                best = min(first, second)
                prices[i-4] = trades[i-4]
                lowestPrice = min(lowestPrice, prices[i-3])
            elif i > 2:
                best = min(0, prices[i-1] + trades[i-3])
            else:
                best = min(prices[:i+1])
            lowestPrice = min(lowestPrice, prices[i])
            trade = min(best, lowestPrice) - prices[i]
            res = min(res, trade)
            trades[i] = min(trade, res)
            print(res)
        print(prices)
        print(trades)
        return abs(res)


prices = [1, 4, 2]
output = 3

prices = [3, 3, 5, 0, 0, 3, 1, 4]
output = 6

# prices = [6, 1, 3, 2, 4, 7]
# output = 6

# prices = [2, 1, 2, 1, 0, 1, 2]
# output = 3

# backwards = [6, 6, 5, 5, 3, 0]
# lowest [6, 1, 1, 1, 1, 1]
# prices = [6, 1, 3, 2, 4, 7]
# output = 6

# lowest ignoring jumps [1, 1, 1, -2, -2]
# lowest factoring jumps [1, 1, 2, -1, -1]
# [1-1=0, 2-1=1, 3-1=2, 0-1=-1, 2--1=3]
# [0, -1, -2, -2, -4]

# prices = [1, 2, 3, 0, 2]
# output = 3

# prices = [1, 2, 4]
# output = 3

# prices = [2, 1]
# output = 0

# prices = [1, 2, 4, 4, 4, 4]
# output = 3


obj = Solution()
res = obj.maxProfit(prices)
print(res)
print(res == output)
