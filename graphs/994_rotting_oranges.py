class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return None
        lenR, lenC = len(grid), len(grid[0])
        arr = [(r, c) for r in range(lenR)
               for c in range(lenC) if grid[r][c] == 2]

        temp = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set(arr)
        minutes = -1
        while arr:
            r, c = arr.pop(0)
            for dR, dC in directions:
                newR, newC = r + dR, c+dC
                if (-1 < newR < lenR) and (-1 < newC < lenC) and grid[newR][newC] > 0 and (newR, newC) not in visited:
                    visited.add((newR, newC))
                    temp.append((newR, newC))
                    grid[newR][newC] = 2
            if not arr:
                arr = temp
                temp = []
                minutes += 1

        for ar in grid:
            for v in ar:
                if v == 1:
                    return -1
        if not visited:
            return 0
        return minutes


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
output = 4

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
output = -1

grid = [[0]]
output = 0

grid = [[1]]
output = -1

obj = Solution()
res = obj.orangesRotting(grid)
print(res)
print(res == output)
