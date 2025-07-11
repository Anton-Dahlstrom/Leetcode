class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j >= len(res):
                    res.append(len(str(grid[i][j])))
                else:
                    res[j] = max(res[j], len(str(grid[i][j])))
        return res


grid = [[1], [22], [333]]
output = [3]

obj = Solution()
res = obj.findColumnWidth(grid)
print(res)
print(output)
print(res == output)
