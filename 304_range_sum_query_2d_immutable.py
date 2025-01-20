class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        for i in range(len(matrix)):
            matrix[i] = [0] + matrix[i]

        matrix.insert(0, [0]*(len(matrix[0])))
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row-1][col] + matrix[row][col -
                                                                    1] + matrix[row][col] - matrix[row-1][col-1]
        self.matrix = matrix.copy()
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.matrix[row2][col2] + self.matrix[row1-1][col1-1] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2]


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
    1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
