class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = [0]*len(prices)

        for i in reversed(range(0, len(prices)-1)):
            price = prices[i]
            if price < prices[i+1]:
                memo[i] = prices[i+1] - price

        print(prices)
        print(memo)
        if len(memo) < 4:
            return sum(memo)
        for i in range(3, len(memo)):
            print(i, prices[i] - min(prices[:i]), max(memo[i-4], memo[i-3],
                                                      memo[i-3] + memo[i-4]) + memo[i])
            memo[i] = max(prices[i] - min(prices[:i]), max(memo[i-4], memo[i-3],
                                                           memo[i-3] + memo[i-4]) + memo[i])
        print(memo)
        return max(memo)


prices = [2, 1, 2, 1, 0, 1, 2]
output = 3

# [6,6,5,5,3,0]
# prices = [6, 1, 3, 2, 4, 7]
# output = 6

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
