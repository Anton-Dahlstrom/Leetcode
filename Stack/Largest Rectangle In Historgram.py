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
        stack = [] #height, index, open
        largest = 0
        toPop = []
        for i, value in enumerate(heights):
            stack.append([value, i])
            for j, rectangle in enumerate(stack):
                if value < rectangle[0]:
                    size = (rectangle[0] * i + 1 - rectangle[1])
                    if size > largest:
                        print(largest)
                        largest = size
                    toPop.append(j)

            if toPop:
                for index in toPop:
                    print(stack, index)
                    stack.pop(index)
                toPop = []

        for rectangle in stack:
            print(largest)
            size = (rectangle[0] * i + 1 - rectangle[1])
            if size > largest:
                largest = size
        return largest
    
obj = Solution()
answer = obj.largestRectangleArea(heights)
print(answer)