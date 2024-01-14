heights =[4,2,0,3,2,4,3,4]
# Answer: 10

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] #height, index
        largest = 0
        for i, value in enumerate(heights):
            stack.append([value, i])
            while len(stack) > 1:
                top = stack[-1]
                if top[0] < stack[-2][0]:
                    under = stack.pop(-2)
                    size = under[0] * (i - under[1])
                    print(largest)
                    largest = max(largest, size)
                    top[1] = under[1]
                    continue
                else:
                    break
        while stack:
            rect = stack.pop(-1)
            size = rect[0] * (i + 1 - rect[1])
            largest = max(largest, size)
        return largest
    
obj = Solution()
answer = obj.largestRectangleArea(heights)
print(answer)