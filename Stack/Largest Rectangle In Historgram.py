heights = [2,1,5,6,2,3]
# output = 10

# Move the pointer on the lowest height and calculate the largest possible 
# rectangle they can make each turn.
# Need to save what the lowest column have been since it's the height multiplier.
# If a pointer runs into a lower height the height of the lowest column for that
# rectangle has to change.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        searching = True
        while searching:
            l = 0
            r = len(heights)-1
            print(heights[l], heights[r])
            break

obj = Solution()
answer = obj.largestRectangleArea(heights)
print(answer)