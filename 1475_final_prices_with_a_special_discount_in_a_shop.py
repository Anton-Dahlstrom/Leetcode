class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = [0] * len(prices)
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            res[i] = prices[i] - discount
        return res


prices = [8, 4, 6, 2, 3]
output = [4, 2, 4, 2, 3]


obj = Solution()
res = obj.finalPrices(prices)
print(res)
print(output)
print(res == output)
