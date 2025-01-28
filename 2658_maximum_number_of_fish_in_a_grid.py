class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        res = 0
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]

        def isValid(r, c):
            if r in range(len(grid)) and c in range(len(grid[0])):
                return True
            return False

        def dfs(r,c): 
            if not grid[r][c]:
                return 0
            total = 0
            total += grid[r][c]
            grid[r][c] = 0
            for nrow, ncol in directions:
                nrow += r
                ncol += c
                if isValid(nrow, ncol) and grid[nrow][ncol]:
                    total += dfs(nrow, ncol)
            return total

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(dfs(r,c), res)

        return res


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
output = 7

obj = Solution()
res = obj.findMaxFish(grid)
print(res)
print(output)
print(res == output)
