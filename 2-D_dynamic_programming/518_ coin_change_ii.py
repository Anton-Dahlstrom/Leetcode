class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        self.res = 0

        def dfs(i, cur):
            print(i, cur)
            if cur == amount:
                self.res += 1
                return
            for j in range(i, len(coins)):
                if cur + coins[j] > amount:
                    return
                dfs(j, cur + coins[j])
        dfs(0, 0)
        return self.res


amount = 500
coins = [3, 5, 7, 8, 9, 10, 11]
output = 500

amount = 5
coins = [1, 2, 5]
output = 4


obj = Solution()
res = obj.change(amount, coins)
print(res)
print(res == output)
