class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        arr = [1] + [0]*amount
        for coin in coins:
            for i in range(len(arr)):
                if arr[i] and i + coin < len(arr):
                    arr[i+coin] += arr[i]
        return arr[-1]


amount = 100
coins = [3, 5, 7, 8, 9, 10, 11]
output = 6606


obj = Solution()
res = obj.change(amount, coins)
print(res)
print(res == output)
