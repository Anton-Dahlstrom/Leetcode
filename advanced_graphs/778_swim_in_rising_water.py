import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        visited = set()
        heap = [[grid[0][0], (0, 0)]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(height, coord):
            print(height, coord)
            print(heap)
            r, c = coord
            if grid[r][c] > height or coord in visited:
                return
            if coord == (len(grid), len(grid[0])):
                return True
            visited.add(coord)

            for d in directions:
                newR, newC = d
                newR += r
                newC += c
                if (-1 < newR < len(grid)) and (-1 < newC < len(grid[0])):
                    print(newR, newC)
                    heapq.heappush(heap, [grid[newR][newC], coord])
                    dfs(height, (newR, newC))
        print(heap)
        while heap:
            height, coord = heap.pop()
            if dfs(height, coord):
                return height
        return False
        # dfs((0,0), grid[0][0])


grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
    12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
output = 16

obj = Solution()
res = obj.swimInWater(grid)
print(res)
print(res == output)
