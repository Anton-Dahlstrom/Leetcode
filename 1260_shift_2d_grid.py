class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[0]*cols for row in range(rows)]
        size = rows*cols
        for row in range(rows):
            for col in range(cols):
                # 0 indexed
                index = ((row*cols) + col + k) % size
                new_row = (index//cols)
                new_col = (index % cols)
                res[new_row][new_col] = grid[row][col]
        return res


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 9
output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

obj = Solution()
res = obj.shiftGrid(grid, k)
print(res)
print(output)
print(res == output)
