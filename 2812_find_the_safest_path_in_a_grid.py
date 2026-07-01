import heapq
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        arr = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)
        visited = set()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    arr.append((row, col))
                    visited.add((row, col))

        def isValid(r, c):
            return r in range(0, n) and c in range(0, n) and (r, c) not in visited

        distance = 0
        while arr:
            temp = []
            for r, c in arr:
                grid[r][c] = distance
                for drow, dcol in directions:
                    nrow, ncol = r+drow, c+dcol
                    if isValid(nrow, ncol):
                        temp.append((nrow, ncol))
                        visited.add((nrow, ncol))

            arr = temp
            distance += 1

        visited = {(0, 0)}
        heap = []
        cur = (-1 * grid[0][0], 0, 0)
        res = float("inf")
        while True:
            dist, r, c = cur[0], cur[1], cur[2]
            res = min(res, -dist)
            if (r, c) == (n-1, n-1):
                break
            for drow, dcol in directions:
                nrow, ncol = r+drow, c+dcol
                if isValid(nrow, ncol):
                    visited.add((nrow, ncol))
                    heapq.heappush(heap, (-1 * grid[nrow][ncol], nrow, ncol))
            cur = heapq.heappop(heap)
        return res
