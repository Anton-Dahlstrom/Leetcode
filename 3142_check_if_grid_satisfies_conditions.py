from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if i < len(grid)-1:
                    if grid[i][j] != grid[i+1][j]:
                        return False
                if j < len(grid[i])-1:
                    if grid[i][j] == grid[i][j+1]:
                        return False
        return True


grid = [[1, 0, 2], [1, 0, 2]]  # True
# grid = [[1, 1, 1], [0, 0, 0]]  # False
# grid = [[1], [2], [3]]  # False
# grid = [[1, 1, 6, 1, 4, 6, 3, 1, 0, 7]]  # False

obj = Solution()
res = obj.satisfiesConditions(grid)
print(res)
