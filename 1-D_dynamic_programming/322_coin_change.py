from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        self.best = float("inf")

        def dfs(i, amount, count):
            if count > self.best:
                return
            if amount < 0:
                return
            if amount == 0:
                self.best = min(self.best, count)
            if i >= len(coins):
                return
            coin = coins[i]
            maxCoin = amount // coin
            i += 1
            for j in reversed(range(0, maxCoin+1)):
                for k in range(i, len(coins)+1):
                    dfs(k, amount - (coin * j), count + j)
        dfs(0, amount, 0)
        if self.best == float("inf"):
            return -1
        return self.best


coins = [1, 2, 5]
amount = 11
output = 3

coins = [1]
amount = 1
coins = [186, 419, 83, 408]
amount = 6249
output = 20

# coins = [1, 2147483647]
# amount = 2
# output = 2

coins = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]
amount = 9864
output = 24

obj = Solution()
res = obj.coinChange(coins, amount)
print(res)
