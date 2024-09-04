class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, columns = set(), set()
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    rows.add(row)
                    columns.add(column)
        for row in rows:
            for column in range(len(matrix[row])):
                matrix[row][column] = 0
        for column in columns:
            for row in range(len(matrix)):
                matrix[row][column] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
output = [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
output = [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


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
        