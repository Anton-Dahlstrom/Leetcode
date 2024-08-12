class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        memo = [0]*len(prices)

        # How much money can be made by buying and instantly selling.
        for i in reversed(range(0, len(prices)-1)):
            price = prices[i]
            # Should save past profits to "reduce" price of buying to find total profit.
            # Should also do all calculations inside this loop.
            if price < prices[i+1]:
                memo[i] = prices[i+1] - price

        print(prices)
        print(memo)
        if len(memo) < 4:
            return sum(memo)
        for i in range(3, len(memo)):
            print(i, prices[i] - min(prices[:i]), max(memo[i-4], memo[i-3],
                                                      memo[i-3] + memo[i-4]) + memo[i])
            # difference in lowest price to current price:
            arg1 = prices[i] - min(prices[:i])
            # best profit we have made in the past plus best profit we can make at this index.
            arg2 = max(memo[i-4], memo[i-3], memo[i-3] + memo[i-4]) + memo[i]
            # best profit in the past plus largest difference in recent price
            arg3 = prices[i] - min(prices[i-2:i]) + max(memo[:i-2])
            memo[i] = max(arg1, arg2, arg3)

            # memo[i] = max(prices[i] - min(prices[:i]), max(memo[i-4], memo[i-3],
            #                                                memo[i-3] + memo[i-4]) + memo[i],
            #               prices[i] - min(prices[i-2:i]) + max(memo[:i-2]))
        print(memo)
        return max(memo)


prices = [2, 1, 2, 1, 0, 1, 2]
output = 3

# backwards = [6, 6, 5, 5, 3, 0]
# lowest [6, 1, 1, 1, 1, 1]
prices = [6, 1, 3, 2, 4, 7]
output = 6

# lowest ignoring jumps [1, 1, 1, -2, -2]
# lowest factoring jumps [1, 1, 2, -1, -1]
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
