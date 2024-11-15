class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        if not buildings:
            return []
        ranges = [[0, float("inf"), 0]]
        for building in buildings:
            left, right, height = building
            i = 0
            while i < len(ranges):
                temp = []
                rleft, rright, rheight = ranges[i]
                if left > rright:
                    continue
                if right < rleft:
                    break
                if height > rheight:
                    if left > rleft:
                        temp.append([rleft, left-1, rheight])
                    temp.append([left, right, height])
                    if right < rright:
                        temp.append([right+1, rright, rheight])
                ranges = ranges[:i] + temp + ranges[i+1:]
                i += len(temp)
        print(ranges)


buildings = [[0, 2, 3], [2, 5, 3]]
output = [[0, 3], [5, 0]]

# buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

obj = Solution()
res = obj.getSkyline(buildings)
print(res)
print(output)
print(res == output)
