class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        rows, cols = m, n
        # guarded, unguarded, guard, wall = -1,0,1,2
        grid = [[0]*cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(r, c, rows, cols):
            return r in range(rows) and c in range(cols)

        res = (rows*cols) - len(guards) - len(walls)
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        for row, col in guards:
            for drow, dcol in directions:
                nrow = row+drow
                ncol = col+dcol
                while isValid(nrow, ncol, rows, cols):
                    if grid[nrow][ncol] > 0:
                        break
                    elif grid[nrow][ncol] == 0:
                        grid[nrow][ncol] = -1
                        res -= 1
                    nrow += drow
                    ncol += dcol

        return res


m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]
output = 7

obj = Solution()
res = obj.countUnguarded(m, n, guards, walls)
print(res)
print(output)
print(res == output)
