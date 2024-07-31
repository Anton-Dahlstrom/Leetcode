import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        visited = set()
        heap = [[grid[0][0], (0, 0)]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(height, coord, first):
            r, c = coord
            if coord in visited and first == False or grid[r][c] > height:
                return
            if coord == (len(grid)-1, len(grid[0])-1):
                return True
            visited.add(coord)

            for d in directions:
                newR, newC = d
                newR += r
                newC += c
                if (-1 < newR < len(grid)) and (-1 < newC < len(grid[0])) and (newR, newC) not in visited:
                    heapq.heappush(heap, [grid[newR][newC], coord])
                    if dfs(height, (newR, newC), False):
                        return True
        while heap:
            height, coord = heapq.heappop(heap)
            if dfs(height, coord, True):
                return height
        return False


grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
    12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
output = 16

obj = Solution()
res = obj.swimInWater(grid)
print(res)
print(res == output)
