import math


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        maxval = math.pow(2, 31)
        n = len(matrix)
        m = len(matrix[0])
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    for newrow in range(n):
                        if matrix[newrow][col] != 0:
                            matrix[newrow][col] = maxval
                    for newcol in range(m):
                        if matrix[row][newcol] != 0:
                            matrix[row][newcol] = maxval

        for row in range(n):
            for col in range(m):
                if matrix[row][col] == maxval:
                    matrix[row][col] = 0
        return


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
output = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


for m in matrix:
    print(m)
print("---------------")
obj = Solution()
obj.setZeroes(matrix)
for m in matrix:
    print(m)
print("-------")
for m in output:
    print(m)
print(matrix == output)
