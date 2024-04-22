from typing import List
import heapq

points = [[1, 3], [-2, 2]]
k = 1
output = [[-2, 2]]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
output = [[3, 3], [-2, 4]]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack = []
        hmap = {}
        for i, coord in enumerate(points):
            sum = 0
            sum += coord[0] * coord[0]
            sum += coord[1] * coord[1]
            sum = sum * -1
            if sum in hmap:
                hmap[sum].append(i)
            else:
                hmap[sum] = [i]

            if len(stack) < k:
                heapq.heappush(stack, sum)
            else:
                removed = heapq.heappushpop(stack, sum)
                hmap[removed].pop()

        stack = []
        for k in hmap:
            if hmap[k]:
                for index in hmap[k]:
                    stack.append(points[index])

        return stack


obj = Solution()
res = obj.kClosest(points, k)
print(res)
