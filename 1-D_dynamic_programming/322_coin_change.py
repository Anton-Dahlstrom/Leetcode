from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        self.best = float("inf")
        temp = [0]*len(coins)
        found = set()
        count = 0
        while temp:
            count += 1
            arr = temp.copy()
            temp = []
            for i in range(0, len(arr)):
                for j in range(0, len(coins)):
                    res = arr[i] + coins[j]
                    if res > amount:
                        continue
                    elif res == amount:
                        return count
                    if res not in found:
                        found.add(res)
                        temp.append(res)
        return -1


# coins = [1, 2, 5]
# amount = 11
# output = 3


# coins = [186, 419, 83, 408]
# amount = 6249
# output = 20

# coins = [1, 2147483647]
# amount = 2
# output = 2

coins = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]
amount = 9864
output = 24

obj = Solution()
res = obj.coinChange(coins, amount)
print(res)
print(res == output)
