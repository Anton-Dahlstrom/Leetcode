import heapq


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        k = len(queries)
        rows = len(grid)
        cols = len(grid[0])

        def isValid(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in visited:
                return True
            return False

        res = [0]*k
        queries = [(queries[i], i) for i in range(k)]
        queries.sort()
        i = 0
        heap = [(grid[0][0], 0, 0)]
        size = 0
        visited = {(0, 0)}
        for i in range(k):
            query, index = queries[i]
            while heap and heap[0][0] < query:
                num, r, c = heapq.heappop(heap)
                size += 1
                for newrow in range(r-1, r+2):
                    if isValid(newrow, c):
                        visited.add((newrow, c))
                        heapq.heappush(
                            heap, (grid[newrow][c], newrow, c))
                for newcol in range(c-1, c+2):
                    if isValid(r, newcol):
                        visited.add((r, newcol))
                        heapq.heappush(
                            heap, (grid[r][newcol], r, newcol))
            res[index] = size
        return res


grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
output = [5, 8, 1]


obj = Solution()
res = obj.maxPoints(grid, queries)
print(res)
print(output)
print(res == output)
