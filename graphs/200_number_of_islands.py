class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        count = 0

        def dfs(grid: list[list[int]], coord: tuple, visited: set):
            y, x = coord
            if y > 0:
                coord = (y-1, x)
                if grid[coord[0]][coord[1]] == "1" and coord not in visited:
                    visited.add(coord)
                    dfs(grid, coord, visited)
            if y < len(grid)-1:
                coord = (y+1, x)
                if grid[coord[0]][coord[1]] == "1" and coord not in visited:
                    visited.add(coord)
                    dfs(grid, coord, visited)
            if x > 0:
                coord = (y, x-1)
                if grid[coord[0]][coord[1]] == "1" and coord not in visited:
                    visited.add(coord)
                    dfs(grid, coord, visited)
            if x < len(grid[0]) - 1:
                coord = (y, x+1)
                if grid[coord[0]][coord[1]] == "1" and coord not in visited:
                    visited.add(coord)
                    dfs(grid, coord, visited)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and (y, x) not in visited:
                    count += 1
                    dfs(grid, (y, x), visited)
        return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
output = 1

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
output = 3

obj = Solution()
res = obj.numIslands(grid)
print(res)
print(res == output)
