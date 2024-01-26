piles = [3,6,7,11]
h = 8
Output: 4

# Sort the array
# Look at the hours minus the length of the array. If they're the same return the biggest pile
# Look at the pile hours minus array from the end of the array.
# If the last pile is less than that pile times two we return the size of the pile we found.
# If not we move each pointer in one step and make sure the piles to the right of the 
# right pointer are less than the left pointers pile times 3.

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        pass


obj = Solution()
answer = obj.search(piles, h)
print(answer)