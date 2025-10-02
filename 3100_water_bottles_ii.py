class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while numBottles:
            res += numBottles
            empty += numBottles
            numBottles = 0
            if empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1
        return res


numBottles = 10
numExchange = 3
output = 13

obj = Solution()
res = obj.maxBottlesDrunk(numBottles, numExchange)
print(res)
print(output)
print(res == output)
