import heapq


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        heap = []
        n = len(startTime)
        for i in range(n):
            event = (startTime[i], endTime[i], profit[i])
            heapq.heappush(heap, event)
        profit = 0
        while heap:
            cur = heapq.heappop(heap)
            if cur[1] == -1:
                profit = max(profit, cur[2])
            else:
                heapq.heappush(heap, (cur[1], -1, cur[2]+profit))
        return profit


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
output = 120

obj = Solution()
res = obj.jobScheduling(startTime, endTime, profit)
print(res)
print(output)
print(res == output)
