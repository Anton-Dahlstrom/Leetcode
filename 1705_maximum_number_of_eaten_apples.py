import heapq


class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        n = len(apples)
        heap = []  # expiration, count
        res = 0
        for i in range(n):
            if apples[i]:
                expires = i + days[i]
                heapq.heappush(heap, [expires, apples[i]])
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if heap:
                res += 1
                heap[0][1] -= 1
                if not heap[0][1]:
                    heapq.heappop(heap)
        day = n
        while heap:
            exp, cnt = heap[0]
            if exp > day:
                eat = min(exp-day, cnt)
                res += eat
                day += eat
            heapq.heappop(heap)
        return res


apples = [1, 2, 3, 5, 2]
days = [3, 2, 1, 4, 2]
output = 7

apples = [9, 2]
days = [3, 5]
output = 5

obj = Solution()
res = obj.eatenApples(apples, days)
print(res)
print(output)
print(res == output)
