# Link: https://leetcode.com/problems/koko-eating-bananas/

piles = [3, 6, 7, 11]
h = 8
Output: 4


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        length = len(piles)
        baseDiv = h // length

        # Gives answers if all values are identical to the smallest or largest pile.
        # The correct answer will lie somewhere inbetween.
        minRate = -(-piles[0] // baseDiv)
        maxRate = -(-piles[-1] // baseDiv)
        midRate = minRate + ((maxRate - minRate)//2)

        # If midRate fits we need to search between midRate and maxRate for the optimal value by updating the value of minRate.
        # Otherwise we search between midRate and minRate by updating maxRate.
        curBest = maxRate
        while minRate <= maxRate:
            midRate = minRate + ((maxRate - minRate)//2)
            res = self.enoughTime(piles, h, midRate)
            if res:
                curBest = midRate
                maxRate = midRate - 1
            else:
                minRate = midRate + 1
        return curBest

    # Checks if Koko has enough time at a given speed.
    def enoughTime(self, piles, h, speed):
        i = 0
        for i in range(len(piles)):
            h -= -(-piles[i]//speed)
            if h < 0:
                return False
        return True


obj = Solution()
answer = obj.minEatingSpeed(piles, h)
print(answer)
