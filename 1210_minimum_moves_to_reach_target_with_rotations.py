class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def isValid(pos):
            row, col = pos
            if row in range(rows) and col in range(cols) and grid[row][col] == 0:
                return True
            return False
        directions = [(1, 0), (0, 1)]

        memo = {}

        def dfs(tail, head, steps):
            # check memo
            if (tail, head) in memo and memo[(tail, head)] <= steps:
                return -1
            memo[(tail, head)] = steps

            # move each direction
            for drow, dcol in directions:
                ntail = (tail[0] + drow, tail[1]+dcol)
                nhead = (head[0] + drow, head[1]+dcol)
                if isValid(ntail) and isValid(nhead):
                    dfs(ntail, nhead, steps+1)

            # try turning
            corner = (tail[0]+1, tail[1]+1)
            if not isValid(corner):
                return

            if tail[0] == head[0]:  # horizontal snake
                head = (tail[0]+1, tail[1])
            else:  # vertical
                head = (tail[0], tail[1]+1)

            if isValid(head):
                dfs(tail, head, steps+1)

        dfs((0, 0), (0, 1), 0)

        target = ((rows-1, cols-2), (rows-1, cols-1))
        if target in memo:
            return memo[target]
        return -1


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]]
output = 11

obj = Solution()
res = obj.minimumMoves(grid)
print(res)
print(output)
print(res == output)
