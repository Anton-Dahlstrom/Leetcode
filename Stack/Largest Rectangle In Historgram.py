heights = [2,1,5,6,2,3]
heights = [2,4]
heights =[0,9]
heights = [2,0,2]

heights =[4,2,0,3,2,4,3,4]
# Answer: 10

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
            if not multiplier:
                multiplier = max(heights[l], heights[r])
                length -= 1
                highest = []
            temp = [multiplier * length, length, multiplier]
            print(multiplier, length)
            print(temp)
            print("L, R", l, r)
            if highest:
                if multiplier < highest[2]:
                    highest[2] = multiplier
                    highest[0] = highest[1]*highest[2]
                if temp[0] > highest[0]:
                    highest = temp
            else:
                highest = temp
            if heights[r] == heights[l]:
                steps = 0
                while r-steps > l+steps:
                    steps += 1
                    if heights[r-steps] > heights[l+steps]:
                        r-=1
                        break
                    elif heights[r-steps] < heights[l+steps]:
                        l+=1
                        break
                    else:
                        steps += 1
            elif heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        if highest:
            return highest[0]
        else:
            return heights[0]
    
obj = Solution()
answer = obj.largestRectangleArea(heights)
print(answer)