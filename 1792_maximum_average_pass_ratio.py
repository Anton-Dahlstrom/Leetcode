import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        classes = [[(((c[0]+1) / (c[1]+1)) - (c[0] / c[1])) * -1] +
                   c for c in classes]
        heapq.heapify(classes)
        for _ in range(extraStudents):
            cur = heapq.heappop(classes)
            cur[1] += 1
            cur[2] += 1
            cur[0] = (((cur[1] + 1) / (cur[2] + 1)) - cur[1] / cur[2]) * -1
            heapq.heappush(classes, cur)

        res = 0
        for c in classes:
            res += c[1] / c[2]
        return res/len(classes)
