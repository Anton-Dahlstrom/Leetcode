class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        grid = [n for arr in grid for n in arr]
        grid.sort()
        target = grid[len(grid)//2]
        remainder = grid[0] % x
        res = 0
        for num in grid:
            if num % x != remainder:
                return -1
            res += abs((num-target)//x)
        return res


grid = [[529, 529, 989], [989, 529, 345], [989, 805, 69]]
x = 92
output = 25

obj = Solution()
res = obj.minOperations(grid, x)
print(res)
print(output)
print(res == output)
