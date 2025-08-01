class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])

        def isValid(row, col):
            if row in range(rows) and col in range(cols) and grid[row][col]:
                return True
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {tuple(start)}
        res = []
        startval = grid[start[0]][start[1]]
        if startval in range(pricing[0], pricing[1]+1):
            res.append(start)

        start = (startval, start[0], start[1])
        arr = [start]
        while arr:
            temp = []
            for _, row, col in arr:
                for drow, dcol in directions:
                    nrow, ncol = row+drow, col+dcol
                    if isValid(nrow, ncol) and (nrow, ncol) not in visited:
                        visited.add((nrow, ncol))
                        val = grid[nrow][ncol]
                        temp.append((val, nrow, ncol))
            temp.sort()
            res += [[val[1], val[2]]
                    for val in temp if val[0] in range(pricing[0], pricing[1]+1)]
            if len(res) >= k:
                return res[:k]
            arr = temp
        return res


grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
pricing = [2, 5]
start = [0, 0]
k = 3
output = [[0, 1], [1, 1], [2, 1]]


obj = Solution()
res = obj.highestRankedKItems(grid, pricing, start, k)
print(res)
print(output)
print(res == output)
