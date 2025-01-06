class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        ones = 0
        steps = 0
        res = [0]*len(boxes)
        for i in range(len(boxes)):
            steps += ones
            res[i] = steps
            if boxes[i] == "1":
                ones += 1
        ones = 0
        steps = 0
        for i in reversed(range(len(boxes))):
            steps += ones
            res[i] += steps
            if boxes[i] == "1":
                ones += 1
        return res


boxes = "110"
output = [1, 1, 3]

obj = Solution()
res = obj.minOperations(boxes)
print(res)
print(output)
print(res == output)
