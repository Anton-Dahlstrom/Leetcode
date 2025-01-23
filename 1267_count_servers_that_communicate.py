class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        cols = {}
        count = 0
        paired = set()
        for r in range(len(grid)):
            temp = set()
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count += 1
                    temp.add((r, c))
                    if c in cols:
                        paired.add((cols[c], c))
                        paired.add((r, c))
                    else:
                        cols[c] = r
            if len(temp) > 1:
                paired.update(temp)

        return len(paired)


grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
output = 4
obj = Solution()
res = obj.countServers(grid)
print(res)
print(output)
print(res == output)
