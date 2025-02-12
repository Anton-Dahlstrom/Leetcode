from collections import defaultdict


class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        n = len(wall)
        options = defaultdict(int)
        for row in range(n):
            size = 0
            for col in range(len(wall[row])-1):
                brick = wall[row][col]
                size += brick
                options[size] += 1
        if not options:
            return n
        return n - max(options.values())


wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
output = 2

# wall = [[2147483647, 2147483647, 2147483647, 2147483647]]
wall = [[1], [1], [1]]

obj = Solution()
res = obj.leastBricks(wall)
print(res)
print(output)
print(res == output)
