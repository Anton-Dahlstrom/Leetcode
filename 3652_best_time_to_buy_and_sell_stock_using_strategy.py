class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        n = len(prices)
        cur = 0
        for i in range(n):
            cur += prices[i] * strategy[i]
        res = cur
        for r in range(n):
            mid = r-(k//2)
            l = r-k
            # sell
            cur += prices[r] - (prices[r]*strategy[r])
            # don't sell
            if mid >= 0:
                cur -= prices[mid]
            # restore
            if l >= 0:
                cur += (prices[l]*strategy[l])
            if r >= k-1:
                res = max(res, cur)
        return res


prices = [4, 2, 8]
strategy = [-1, 0, 1]
k = 2
output = 10


obj = Solution()
res = obj.maxProfit(prices, strategy, k)
print(res)
print(output)
print(res == output)
