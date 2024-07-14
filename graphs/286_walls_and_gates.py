# Solution designed for https://neetcode.io/problems/islands-and-treasure

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return None
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rowLen = len(grid)
        colLen = len(grid[0])
        memo = []

        def bfs():
            visited = set()
            while memo:
                coord = memo.pop(0)
                r, c = coord
                for d in directions:
                    newR, newC = r+d[0], c+d[1]
                    if (-1 < newR < rowLen) and (-1 < newC < colLen) and (newR, newC) not in visited:
                        if grid[newR][newC] in (0, -1):
                            continue
                        memo.append((newR, newC))
                        visited.add((newR, newC))
                        grid[newR][newC] = min(grid[newR][newC], grid[r][c]+1)

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == 0:
                    memo.append((row, col))
                    bfs()
        return grid


grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

output = [
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]


obj = Solution()
res = obj.islandsAndTreasure(grid)
print(res)
print(res == output)
