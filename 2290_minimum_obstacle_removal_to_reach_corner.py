from collections import deque
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        edges = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for y in range(row-1, row+2, 2):
                    if y in range(0, len(grid)):
                        edges.setdefault((row, col),{})[(y, col)] = grid[y][col]
                for x in range(col-1, col+2, 2):
                    if x in range(0, len(grid[0])):
                        edges.setdefault((row, col),{})[(row, x)] = grid[row][x]

        visited = {(0,0): grid[0][0]}
        queue = deque()
        queue.appendleft((0,0))
        while queue:
            coord = queue.pop()
            for edge in edges[coord]:
                curSteps = visited[coord] + grid[edge[0]][edge[1]]
                if edge not in visited:
                    visited[edge] = curSteps
                    queue.appendleft(edge)
                else:
                    if curSteps < visited[edge]:
                        visited[edge] = curSteps
                        queue.appendleft(edge)
        return visited[(len(grid)-1, len(grid[0])-1)]
    

grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
output= 0

obj = Solution()
res = obj.minimumObstacles(grid)
print(output)
print(res)
print(res == output)