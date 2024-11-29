import heapq
class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if (grid[1][0] > 1 and grid[0][1] > 1) or grid[0][0] > 0:
            return -1
        heap = [(1,(0,0))]
        heapq.heapify(heap)
        visited = {(0,0)}
        while heap:
            time, coords = heapq.heappop(heap)
            row, col = coords
            if row == len(grid)-1 and col == len(grid[0])-1:
                return time -1
            for nrow in range(row-1, row+2, 2):
                if nrow in range(0,len(grid)) and (nrow, col) not in visited:
                    visited.add((nrow, col))
                    if grid[nrow][col] > time:
                        newtime = grid[nrow][col]
                        timeDiff = grid[nrow][col] - time
                        if timeDiff % 2:
                            newtime += 1
                        newtime += 1
                    else:
                        newtime = time + 1
                    heapq.heappush(heap, (newtime, (nrow, col)))
                        
            for ncol in range(col-1, col+2, 2):
                if ncol in range(0,len(grid[0])) and (row, ncol) not in visited:
                    visited.add((row, ncol))
                    if grid[row][ncol] > time:
                        newtime = grid[row][ncol]
                        timeDiff = grid[row][ncol] - time
                        if timeDiff % 2:
                            newtime += 1
                        newtime += 1
                    else:
                        newtime = time + 1
                    heapq.heappush(heap, (newtime, (row, ncol)))

grid = [[0,1,3,2],
        [5,1,2,5],
        [4,3,8,6]]
output = 7

obj = Solution()
res = obj.minimumTime(grid)
print(res)
print(output)
print(res == output)