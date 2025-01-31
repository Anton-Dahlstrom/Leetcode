class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        rank = [0]*(len(grid) * len(grid[0]))
        parents = [(r*len(grid[0]))+c for r in range(len(grid)) for c in range(len(grid[0]))]

        def findParent(node):
            if parents[node] != node:
                parents[node] = findParent(parents[node])


        def isValid(r,c):
            if r in range(len(grid)) and c in range(len(grid[0])):
                return True

        res = 1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cur = r*len(grid[0])+c
                if grid[r][c] == 0 or parents[cur] != cur:
                    continue
                arr = [(r,c)]
                rank[cur] = 1
                while arr:
                    temp = []
                    while arr:
                        row,col = arr.pop()
                        for d in directions:
                            nrow, ncol = d
                            nrow += row
                            ncol += col
                            node = nrow*len(grid[0])+ncol
                            if isValid(nrow,ncol) and grid[nrow][ncol] == 1 and (nrow, ncol) != (r,c) and parents[node] == node:
                                parents[node] = cur 
                                rank[cur] +=1
                                temp.append((nrow, ncol))
                    arr = temp
                res = max(res, rank[cur])
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    continue
                setparents = set()
                size = 1
                for d in directions:
                    nrow, ncol = d
                    nrow += r
                    ncol += c
                    if isValid(nrow, ncol) and grid[nrow][ncol] == 1:
                        node = nrow*len(grid[0])+ncol
                        parent = parents[node]
                        if parent not in setparents:
                            size += rank[parent]
                        setparents.add(parent)
                res = max(size, res)
        return res

grid = [[1,0],[0,1]]
output= 3

grid = [[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]]
output = 18

obj = Solution()
res = obj.largestIsland(grid)
print(res)
print(output)
print(res == output)
        