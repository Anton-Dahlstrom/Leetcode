heights = [2,1,5,6,2,3]
heights = [2,4]
heights =[0,9]
# output = 10

# Move the pointer on the lowest height and calculate the largest possible 
# rectangle they can make each turn.
# Need to save what the lowest column have been since it's the height multiplier.
# If a pointer runs into a lower height the height of the lowest column for that
# rectangle has to change.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        highest = []
        l = 0
        r = len(heights)-1
        while r > l:
            print(heights[l], heights[r])
            length = r - l + 1
            multiplier = min(heights[l], heights[r])
            temp = [multiplier * length, length, multiplier]
            print(multiplier, length)
            print(temp)
            if highest:
                if multiplier < highest[2]:
                    highest[2] = multiplier
                    highest[0] = highest[1]*highest[2]
                if temp[0] > highest[0]:
                    highest = temp
                if heights[r] > heights[l]:
                    l+=1
                else:
                    r-=1
            else:
                highest = temp
        if highest:
            return highest[0]
        else:
            return heights[0]
    
obj = Solution()
answer = obj.largestRectangleArea(heights)
print(answer)