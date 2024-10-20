class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row + col == 0:
                    if obstacleGrid[row][col] == 1:
                        return 0
                    obstacleGrid[row][col] = 1
                elif obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    if col > 0:
                        obstacleGrid[row][col] += obstacleGrid[row][col-1]
                    if row > 0:
                        obstacleGrid[row][col] += obstacleGrid[row-1][col]

        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
output = 2

obj = Solution()
res = obj.uniquePathsWithObstacles(obstacleGrid)
print(res)
print(output)
print(res == output)
