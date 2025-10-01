class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            drink = numBottles - (numBottles % numExchange)
            res += drink
            numBottles -= drink
            numBottles += drink//numExchange
        return res + numBottles


numBottles = 15
numExchange = 4
output = 19

obj = Solution()
res = obj.numWaterBottles(numBottles, numExchange)
print(res)
print(output)
print(res == output)
