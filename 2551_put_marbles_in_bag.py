import heapq


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        base = weights[0] + weights[-1]
        if k == 1:
            return 0
        maxheap = []
        minheap = []
        for i in range(1, n):
            pair = weights[i] + weights[i-1]
            if len(maxheap) >= k-1:
                if pair > maxheap[0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, pair)
                if pair*-1 > minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, pair*-1)
            else:
                heapq.heappush(maxheap, pair)
                heapq.heappush(minheap, pair*-1)
        maxres = base
        minres = base
        for i in range(len(maxheap)):
            maxres += maxheap[i]
            minres += minheap[i]*-1
        return maxres - minres


weights = [1, 3, 5, 1]
k = 2
output = 4

weights = [54, 6, 34, 66, 63, 52, 39, 62, 46, 75, 28, 65,
           18, 37, 18, 13, 33, 69, 19, 40, 13, 10, 43, 61, 72]
k = 4
output = 289


obj = Solution()
res = obj.putMarbles(weights, k)
print(res)
print(output)
print(res == output)
