class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            row, col = i, 0
            turn = 0
            temp = []
            while row < rows and col < cols:
                temp.append((grid[row][col], turn))
                turn += 1
                row += 1
                col += 1
            temp.sort(reverse=True)
            row, col = i, 0
            turn = 0
            while row < rows and col < cols:
                grid[row][col] = temp[turn][0]
                turn += 1
                row += 1
                col += 1

        for i in range(1, cols):
            row, col = 0, i
            turn = 0
            temp = []
            while row < rows and col < cols:
                temp.append((grid[row][col], turn))
                turn += 1
                row += 1
                col += 1
            temp.sort()
            row, col = 0, i
            turn = 0
            while row < rows and col < cols:
                grid[row][col] = temp[turn][0]
                turn += 1
                row += 1
                col += 1
        return grid


grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
output = [[8, 2, 3], [9, 6, 7], [4, 5, 1]]

obj = Solution()
res = obj.sortMatrix(grid)
print(res)
print(output)
print(res == output)
