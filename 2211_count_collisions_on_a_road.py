class Solution:
    def countCollisions(self, directions: str) -> int:
        leftCars = False
        cur = 0
        res = 0
        for car in directions:
            if car == "L":
                if leftCars:
                    res += 1
                res += cur
                cur = 0
            elif car == "S":
                res += cur
                cur = 0
                leftCars = True
            elif car == "R":
                cur += 1
                leftCars = True

        return res


directions = "RLRSLL"
output = 5

obj = Solution()
res = obj.countCollisions(directions)
print(res)
print(output)
print(res == output)
