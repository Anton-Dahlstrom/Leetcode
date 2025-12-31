class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        # go backwards and find first day where you can cross
        n = len(cells)
        grid = [[0 for _ in range(col)] for _ in range(row)]
        for r, c in cells:
            grid[r-1][c-1] = 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isInGrid(r, c):
            if r in range(row) and c in range(col):
                return True
            return False

        parents = {}

        for r in range(row):
            for c in range(col):
                parents[(r, c)] = (r, c)

        def findParent(cur):
            parent = parents[cur]
            # parents parent is source of truth
            if parents[parent] != parent:
                findParent(parent)
                parents[cur] = parents[parent]
            return parents[cur]

        def connectSets(r, c):
            grid[r][c] = 0
            for drow, dcol in directions:
                nrow, ncol = r+drow, c+dcol
                if isInGrid(nrow, ncol) and grid[nrow][ncol] == 0:
                    findParent((r, c))
                    findParent((nrow, ncol))

                    p1, p2 = parents[(r, c)], parents[(nrow, ncol)]
                    if min(p1[0], p2[0]) == 0 and max(p1[0], p2[0]) == row-1:
                        return True

                    nextpar = p1
                    if p1[0] != row-1 and (p2[0] == row-1 or p2[0] < p1[0]):
                        nextpar = p2
                    parents[parents[(r, c)]] = nextpar
                    parents[parents[(nrow, ncol)]] = nextpar
            return False

        for day in range(n-1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            if connectSets(r, c):
                return day


row = 4
col = 3
cells = [[3, 2], [2, 1], [1, 3], [1, 2], [3, 3], [2, 2],
         [4, 3], [1, 1], [2, 3], [4, 1], [3, 1], [4, 2]]
output = 3

obj = Solution()
res = obj.latestDayToCross(row, col, cells)
print(res)
print(output)
print(res == output)
