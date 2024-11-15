class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        if not buildings:
            return []
        heights = []
        for building in buildings:
            left, right, height = building
            if right > len(heights):
                heights += [0]*(right - len(heights) + 1)
            for i in range(left, right):
                heights[i] = max(heights[i], height)

        res = []
        prevHeight = 0
        for i in range(0, len(heights)):
            if heights[i] != prevHeight:
                prevHeight = heights[i]
                temp = [i, heights[i]]
                res.append(temp)
        return res


buildings = [[0, 2, 3], [2, 5, 3]]
output = [[0, 3], [5, 0]]

buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

obj = Solution()
res = obj.getSkyline(buildings)
print(res)
print(output)
print(res == output)
