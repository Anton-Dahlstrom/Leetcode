class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        def checkRow(row, left, right):
            for col in range(left, right):
                if not matrix[row][col]:
                    return False
            return True

        def checkCol(col, top, bottom):
            for row in range(top, bottom):
                if not matrix[row][col]:
                    return False
            return True

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for row in range(rows):
            for col in range(cols):
                size = 1
                while row+size <= rows and col+size <= cols:
                    if not checkRow(row+size-1, col, col+size) or not checkCol(col+size-1, row, row+size):
                        break
                    res += 1
                    size += 1
        return res


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
output = 15

obj = Solution()
res = obj.countSquares(matrix)
print(res)
print(output)
print(res == output)
