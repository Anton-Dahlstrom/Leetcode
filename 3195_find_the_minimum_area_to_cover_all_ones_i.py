class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        left, top, right, bot = cols, rows, -1, -1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    if col < left:
                        left = col
                    if col > right:
                        right = col
                    if row < top:
                        top = row
                    if row > bot:
                        bot = row
        return (bot-top+1)*(right-left+1)


grid = [[0, 1, 0], [1, 0, 1]]
output = 6

obj = Solution()
res = obj.minimumArea(grid)
print(res)
print(output)
print(res == output)
