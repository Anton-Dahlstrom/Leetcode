class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        smallest = float("inf")
        res = 0
        oddNegative = False
        for m in matrix:
            for num in m:
                if num < 0 and smallest:
                    oddNegative = oddNegative == False
                num = abs(num)
                if smallest:
                    smallest = min(smallest, num)
                res += num
        if oddNegative and smallest:
            res += (smallest * 2)*-1
        return res


matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
output = 16

matrix = [[1, -1], [-1, 1]]
output = 4

matrix = [[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]
output = 15

matrix = [[2, 9, 3], [5, 4, -4], [1, 7, 1]]
output = 34

obj = Solution()
res = obj.maxMatrixSum(matrix)
print(res)
print(output)
print(res == output)
