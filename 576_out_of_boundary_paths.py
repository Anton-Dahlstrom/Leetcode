class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        visited = {}

        def dfs(r, c, moves):
            if (r, c, moves) in visited:
                return visited[(r, c, moves)]
            if r < 0 or r >= m:
                return 1
            if c < 0 or c >= n:
                return 1
            if moves == maxMove:
                return 0

            res = 0
            for nrow in range(-1, 2, 2):
                res += dfs(nrow+r, c, moves+1)
            for ncol in range(-1, 2, 2):
                res += dfs(r, ncol+c, moves+1)
            visited[(r, c, moves)] = res
            return res

        return dfs(startRow, startColumn, 0) % (10**9 + 7)


m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
output = 6

obj = Solution()
res = obj.findPaths(m, n, maxMove, startRow, startColumn)
print(res)
print(output)
print(res == output)
