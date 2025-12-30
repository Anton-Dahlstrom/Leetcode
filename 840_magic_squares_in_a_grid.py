class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def isMagical(r, c):
            # Check unique
            unique = set()
            for row in range(r-1, r+2):
                for col in range(c-1, c+2):
                    num = grid[row][col]
                    if num not in range(1, 10) or num in unique:
                        return False
                    unique.add(grid[row][col])

            target = 15
            # Check rows
            for row in range(r-1, r+2):
                if sum(grid[row][c-1:c+2]) != target:
                    return False

            # Check cols
            for col in range(c-1, c+2):
                cur = 0
                for row in range(r-1, r+2):
                    cur += grid[row][col]
                if cur != target:
                    return False

            # Check diagonals
            d1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
            d2 = grid[r+1][c-1] + grid[r][c] + grid[r-1][c+1]
            if d1 != target or d2 != target:
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        res = 0
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if isMagical(row, col):
                    res += 1
        return res


grid = [[10, 3, 5],
        [1, 6, 11],
        [7, 9, 2]]
output = 0

obj = Solution()
res = obj.numMagicSquaresInside(grid)
print(res)
print(output)
print(res == output)
