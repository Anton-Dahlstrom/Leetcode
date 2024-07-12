class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        largest = 0
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        ylen = len(grid)
        xlen = len(grid[0])

        def dfs(coord):
            y, x = coord
            for dir in directions:
                nexty, nextx = y+dir[0], x+dir[1]
                if nexty in range(ylen) and nextx in range(xlen) and (nexty, nextx) not in visited and grid[nexty][nextx] == 1:
                    visited.add((nexty, nextx))
                    dfs((nexty, nextx))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1 and (y, x) not in visited:
                    start = len(visited)
                    dfs((y, x))
                    visited.add((y, x))
                    largest = max(largest, len(visited) - start)
        return largest


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
output = 6

grid = [[1]]
output = 1

obj = Solution()
res = obj.maxAreaOfIsland(grid)
print(res)
print(res == output)
