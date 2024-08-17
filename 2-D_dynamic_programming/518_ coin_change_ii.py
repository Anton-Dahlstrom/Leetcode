class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        res = 0
        stack = [amount]
        while stack:
            print(stack)
            cur = stack.pop()
            for c in coins:
                temp = cur - c
                if temp == 0:
                    print("adding", cur, c)
                    res += 1
                elif temp > 0:
                    stack.append(temp)
        print(stack)
        print(res)
        return


amount = 20
coins = [3, 5, 7, 8, 9, 10, 11]
output = 20

amount = 5
coins = [1, 2, 5]
output = 4


obj = Solution()
res = obj.change(amount, coins)
print(res)
print(res == output)
