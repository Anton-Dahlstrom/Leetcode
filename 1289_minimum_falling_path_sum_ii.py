class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        i1 = -1
        i2 = -1
        for row in range(0, n):
            min1 = float("inf")
            min2 = float("inf")
            for col in range(n):
                val = grid[row][col]
                if val < min2:
                    min2 = val
                    i2 = col
                if min2 < min1:
                    min1, min2 = min2, min1
                    i1, i2 = i2, i1
            if row == n-1:
                return min1

            for col in range(n):
                if col != i1:
                    grid[row+1][col] += min1
                else:
                    grid[row+1][col] += min2


grid = [[-73, 61, 43, -48, -36], [3, 30, 27, 57, 10],
        [96, -76, 84, 59, -15], [5, -49, 76, 31, -7], [97, 91, 61, -46, 67]]
output = -192

obj = Solution()
res = obj.minFallingPathSum(grid)
print(res)
print(output)
print(res == output)
