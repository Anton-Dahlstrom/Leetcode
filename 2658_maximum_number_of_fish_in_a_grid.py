class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        res = 0
        visited = set()

        def dfs(pos):
            visited.add(pos)
            r, c = pos
            total = grid[r][c]
            for nr in range(r-1, r+2, 2):
                if nr in range(0, len(grid)) and (nr, c) not in visited and grid[nr][c] > 0:
                    total += dfs((nr, c))
            for nc in range(c-1, c+2, 2):
                if nc in range(0, len(grid[0])) and (r, nc) not in visited and grid[r][nc] > 0:
                    total += dfs((r, nc))
            return total

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0 and (r, c) not in visited:
                    res = max(res, dfs((r, c)))

        return res


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
output = 7

obj = Solution()
res = obj.findMaxFish(grid)
print(res)
print(output)
print(res == output)
