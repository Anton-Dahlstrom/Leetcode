import heapq


class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        grid = isInfected
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inGrid(pos):
            row, col = pos
            if row in range(rows) and col in range(cols):
                return True
            return False

        def dfs(row, col):
            visited.add((row, col))
            walls = 0
            for drow, dcol in directions:
                nrow, ncol = (row+drow, col+dcol)
                pos = (nrow, ncol)
                if inGrid(pos) and pos not in visited:
                    if grid[nrow][ncol] == 0:
                        willInfect.add(pos)
                        walls += 1
                    elif grid[nrow][ncol] == 1:
                        walls += dfs(nrow, ncol)
            return walls

        def quarantine(row, col):
            visited.add((row, col))
            grid[row][col] = -1
            for drow, dcol in directions:
                nrow, ncol = (row+drow, col+dcol)
                pos = (nrow, ncol)
                if inGrid(pos) and grid[nrow][ncol] == 1:
                    quarantine(nrow, ncol)

        res = 0
        while True:
            visited = set()
            heap = []
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1 and (row, col) not in visited:
                        willInfect = set()
                        walls = dfs(row, col)
                        heapq.heappush(
                            heap, (-len(willInfect), (row, col), willInfect, walls))
            if not heap:
                return res
            containing = heapq.heappop(heap)
            res += containing[3]
            visited = set()
            quarantine(containing[1][0], containing[1][1])
            while heap:
                cur = heapq.heappop(heap)
                for r, c in cur[2]:
                    grid[r][c] = 1


isInfected = [[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
output = 10

obj = Solution()
res = obj.containVirus(isInfected)
print(res)
print(output)
print(res == output)
