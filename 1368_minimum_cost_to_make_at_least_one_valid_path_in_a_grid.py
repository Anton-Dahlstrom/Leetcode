import heapq


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        hmap = {(0, 0): 0}
        heap = [(0, 0, 0)]  # cost, row, col

        while heap:
            cost, row, col = heapq.heappop(heap)
            for i in range(len(directions)):
                nrow, ncol = directions[i]
                nrow += row
                ncol += col
                if nrow in range(0, len(grid)) and ncol in range(0, len(grid[0])):
                    ncost = cost
                    if grid[row][col] != i+1:
                        ncost += 1
                    if (nrow, ncol) in hmap:
                        if ncost >= hmap[(nrow, ncol)]:
                            continue
                    hmap[(nrow, ncol)] = ncost
                    heapq.heappush(heap, (ncost, nrow, ncol))
        return hmap[(len(grid)-1, len(grid[0])-1)]


grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
output = 3

obj = Solution()
res = obj.minCost(grid)
print(res)
print(output)
print(res == output)
