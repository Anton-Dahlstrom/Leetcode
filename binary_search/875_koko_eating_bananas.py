# Link: https://leetcode.com/problems/koko-eating-bananas/

from math import ceil
piles = [3, 6, 7, 11]
h = 8
Output: 4

# piles = [30, 11, 23, 4, 20]
# h = 5
# Output: 30
# Sort the array
# Look at the hours minus the length of the array. If they're the same return the biggest pile
# Look at the pile hours minus array from the end of the array.
# If the last pile is less than that pile times two we return the size of the pile we found.
# If not we move each pointer in one step and make sure the piles to the right of the
# right pointer are less than the left pointers pile times 3.

# Need to see how many times the array fits in the hours and then see how many leftover hours there are
# Then we look at how the numbers can be divided amongst eachother


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        length = len(piles)
        baseDivision = h // length
        extraDivision = h % length
        print(baseDivision, extraDivision)
        print(piles[-1])
        # Solution without worrying about extraDivisions
        if piles[0] == piles[-1]:
            return ceil(piles / 2)


obj = Solution()
answer = obj.minEatingSpeed(piles, h)
print(answer)
