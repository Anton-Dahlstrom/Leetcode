class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        n = len(instructions)
        # north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        for i in range(n*4):
            j = i % n
            ins = instructions[j]
            if ins == "G":
                nx, ny = directions[direction]
                x, y = x+nx, y+ny
            elif ins == "R":
                direction = (direction+1) % 4
                pass
            elif ins == "L":
                direction = (direction-1) % 4

        if not x and not y:
            return True
        return False


instructions = "GGLLGG"
output = True

obj = Solution()
res = obj.isRobotBounded(instructions)
print(res)
print(output)
print(res == output)
