class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2:
            low -= 1

        if high % 2:
            high += 1
        return (high-low)//2


low = 3
high = 7
output = 3

obj = Solution()
res = obj.countOdds(low, high)
print(res)
print(output)
print(res == output)
