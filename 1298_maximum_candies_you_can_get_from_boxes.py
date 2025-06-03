class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        # status:
        # 0 = nothing found
        # 1 = found key
        # 2 = found box
        # 3 = opened
        n = len(status)
        res = 0
        arr = initialBoxes
        while arr:
            temp = []
            for box in arr:
                if status[box] == 3:
                    continue
                elif status[box] == 1:
                    res += candies[box]
                    status[box] = 3
                elif status[box] == 0:
                    status[box] = 2

                for newbox in containedBoxes[box]:
                    if status[newbox] == 0:
                        status[newbox] = 2
                    elif status[newbox] == 1:
                        temp.append(newbox)
                for key in keys[box]:
                    if status[key] == 2:
                        status[key] = 1
                        temp.append(key)
                    elif status[key] == 0:
                        status[key] = 1
            arr = temp

        return res


status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
output = 16

obj = Solution()
res = obj.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
print(res)
print(output)
print(res == output)
